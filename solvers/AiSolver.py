import tensorflow

from objects.Space import Space
from functions.loss.LossFunction import LossFunction
from tqdm import tqdm

class AiSolver:
    def __init__(self,variables: Space,solution_function,loss_function:LossFunction,learning_rate:float):
        self.space = variables
        self.variables = variables.split()
        self.solution_function = solution_function
        self.loss_function = loss_function

        self.function = tensorflow.keras.Sequential(
            [tensorflow.keras.layers.Dense(units=32, activation='sigmoid', dtype='float64'),
             tensorflow.keras.layers.Dense(units=1, activation='linear', dtype='float64')])
        self.optimizer = tensorflow.keras.optimizers.Adam(learning_rate=learning_rate)

    def solve(self,epochs:int):
        self.function(self.variables)

        for i in tqdm(range(epochs)):
            with tensorflow.GradientTape() as tape:
                current_loss = self.__loss__()
            gradients = tape.gradient(current_loss, self.function.trainable_variables)
            self.optimizer.apply_gradients(zip(gradients, self.function.trainable_variables))

        print(f"done strata = {self.__loss__().numpy()}")

    def calculate(self, x):
        return self.function(x)

    def __loss__(self):
        return tensorflow.reduce_mean((self.loss_function.calculate(self.solution_function.calculate,self.space)) ** 2)