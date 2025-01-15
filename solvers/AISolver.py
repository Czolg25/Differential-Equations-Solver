import tensorflow
import numpy
from tensorflow.keras import layers

class AISolver:
    def __init__(self,x,y):
        self.neural_network = tensorflow.keras.Sequential([
            layers.Dense(units=20, activation='tanh', dtype='float64'),
            layers.Dense(units=20, activation='tanh', dtype='float64'),
            layers.Dense(units=1, activation='linear', dtype='float64')
        ])
        self.opt = tensorflow.keras.optimizers.Adam(learning_rate=0.01)
        self.x = tensorflow.constant(x, shape=(len(x), 1), dtype='float64')
        self.y =  tensorflow.constant(y, shape=(len(y), 1), dtype='float64')

    def u_approx(self,x, t):
        return self.neural_network(tensorflow.concat([x, t], axis=1))

    def calculate(self):
        print(self.x)
        return self.u_approx(self.x, self.y)

    def __loss(self,x,t):
        with tensorflow.GradientTape(persistent=True) as g:
            g.watch(x)
            g.watch(t)

            # Compute the approximated solution and derivatives
            u = self.u_approx(x, t)
            u_x = g.gradient(u, x)  # First derivative wrt x
            u_xx = g.gradient(u_x, x)  # Second derivative wrt x
            u_t = g.gradient(u, t)  # First derivative wrt t

        # Boundary and initial conditions
        n = 100
        x_bc = tensorflow.concat([tensorflow.zeros((n // 2, 1), dtype=tensorflow.float64), tensorflow.ones((n // 2, 1), dtype=tensorflow.float64)], axis=0)
        t_bc = tensorflow.random.uniform((n, 1), 0, 1, dtype=tensorflow.float64)
        x_ic = tensorflow.random.uniform((n, 1), 0, 1, dtype=tensorflow.float64)
        t_ic = tensorflow.zeros((n, 1), dtype=tensorflow.float64)

        # PDE residual
        pde_residual = u_t - 0.1 * u_xx

        # Mean squared error of the PDE residual
        loss_pde = tensorflow.reduce_mean(pde_residual ** 2)

        # Enforce boundary conditions: u(0, t) = 0, u(1, t) = 0
        loss_bc = tensorflow.reduce_mean(self.u_approx(x_bc, t_bc) ** 2)

        # Enforce initial condition: u(x, 0) = sin(pi * x)
        loss_ic = tensorflow.reduce_mean((self.u_approx(x_ic, t_ic) - tensorflow.sin(numpy.pi * x_ic)) ** 2)

        return loss_pde + loss_bc + loss_ic

    def solve(self,steps:int):
        for i in range(steps):
            with tensorflow.GradientTape() as tape:
                current_loss = self.__loss(self.x,self.y)
            grads = tape.gradient(current_loss, self.neural_network.trainable_variables)
            self.opt.apply_gradients(zip(grads, self.neural_network.trainable_variables))

            # Print progress every 100 steps
            if i % 100 == 0:
                print(f"Step {i}, Loss: {current_loss.numpy()}")