import numpy as np
import tensorflow as tf
from tensorflow.keras import layers


class Krowiak:
    def __init__(self,x):
        self.x = tf.constant(x, shape=(len(x), 1), dtype='float64')
        self.N = tf.keras.Sequential([layers.Dense(units=10, activation='sigmoid', dtype='float64'),
                                 layers.Dense(units=1, activation='linear', dtype='float64')])


    def psi_t(self,x):
        war_pocz = 0
        return war_pocz + x * self.N(x)


    def f(self, psi):
        return np.exp(-1*self.x / 5) * np.cos(self.x) - psi / 5


    def loss(self):
        with tf.GradientTape() as g:
            g.watch(self.x)
            psi_t_ = self.psi_t(self.x)
        psi_p = g.gradient(psi_t_, self.x)

        return tf.reduce_mean((psi_p - self.f( psi_t_)) ** 2)

    def solve(self,m):
        opt = tf.keras.optimizers.Adam(learning_rate=0.1)

        self.N(self.x)  # inicjalizacja sieci

        for i in range(100):
            with tf.GradientTape() as tape:
                current_loss = self.loss()
            grads = tape.gradient(current_loss, self.N.trainable_variables)
            opt.apply_gradients(zip(grads, self.N.trainable_variables))