import tensorflow
import numpy
from tqdm import tqdm

from objects.space.Space import Space
from objects.functions.loss.LossFunction import LossFunction


class AISolver:
    def __init__(self, space: Space, solution_function, loss_function: LossFunction,loss_plot:bool = True):
        self.__neural_network = tensorflow.keras.Sequential([
            tensorflow.keras.layers.Dense(units=10, activation='sigmoid', dtype='float64'),
            tensorflow.keras.layers.Dense(units=1, activation='linear', dtype='float64')])
        self.__optimizer = tensorflow.keras.optimizers.Adam(learning_rate=0.01)
        self.__points = space.get_points_to_neural_network()
        self.__solution_function = solution_function
        self.__loss_function = loss_function
        self.__loss_plot = loss_plot
        self.__loss_array = numpy.array([])

    def calculate(self, *variables):
        return self.__neural_network(*variables)

    def solve(self, epochs: int):
        self.__neural_network(*self.__points)

        for i in tqdm(range(epochs)):
            with tensorflow.GradientTape() as tape:
                current_loss = self.__loss_function.calculate(self.__solution_function, *self.__points)
                if self.__loss_plot:
                    self.__loss_array = numpy.append(self.__loss_array, current_loss.numpy())
            grads = tape.gradient(current_loss, self.__neural_network.trainable_variables)
            self.__optimizer.apply_gradients(zip(grads, self.__neural_network.trainable_variables))

    def get_loss_array(self):
        if self.__loss_plot:
            return self.__loss_array
        return None
