import tensorflow
import numpy
from objects.Range import Range


class Space:
    def __init__(self, numberInOne: int, *ranges: Range):
        self.__ranges = ranges
        self.__numberInOne = numberInOne

    def split(self, multiply: int = 1):
        axes_array = []

        for axe in self.__ranges:
            number_of_split = self.calculate_amount_of_split(axe, self.__numberInOne) * multiply

            axe = numpy.linspace(axe.get_min(), axe.get_max(), number_of_split)
            axe = tensorflow.constant(axe, shape=(number_of_split, 1), dtype='float64')
            axes_array.append(axe[:, 0])

        mesh_grids = tensorflow.meshgrid(*axes_array, indexing='ij')

        reshaped_grids = [tensorflow.reshape(grid, [-1]) for grid in mesh_grids]
        return tensorflow.stack(reshaped_grids, axis=1)

    def get_axis_as_numpy(self, index: int,multiply: int = 1):
        axe = self.__ranges[index]
        number_of_split = self.calculate_amount_of_split(axe, self.__numberInOne) * multiply
        return numpy.linspace(axe.get_min(), axe.get_max(), number_of_split)

    def get_axis_as_tensor(self, index: int, multiply: int = 1):
        axe = self.__ranges[index]
        number_of_split = self.calculate_amount_of_split(axe, self.__numberInOne) * multiply
        return tensorflow.constant(numpy.linspace(axe.get_min(), axe.get_max(), number_of_split), shape=(number_of_split, 1), dtype='float64')

    def calculate_amount_of_split(self, range: Range, numberInOne: int):
        amount = int(float((range.get_max()) - float(range.get_min())) * numberInOne)
        if amount < 10:
            return 11
        return amount + 1

    def get_axis_amount(self):
        return len(self.__ranges)

    def __str__(self):
        string = ""
        for range in self.__ranges:
            string += f"{range},"

        return f'[{string}]'
