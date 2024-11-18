import numpy
import tensorflow

from objects.Range import Range

class Space:

    def __init__(self, numberInOne:int,*ranges:Range):
        self.ranges = ranges
        self.numberInOne = numberInOne

    def split(self):
        axes_array = []

        for range in self.ranges:
            numberOfSplit = self.calculateAmountOfSplit(range, self.numberInOne)

            axe = numpy.linspace(range.get_min(), range.get_max(), numberOfSplit)
            axe = tensorflow.constant(axe, shape=(numberOfSplit, 1), dtype='float64')
            axes_array.append(axe[:, 0])

        mesh_grids = tensorflow.meshgrid(*axes_array, indexing='ij')

        reshaped_grids = [tensorflow.reshape(grid, [-1]) for grid in mesh_grids]
        return tensorflow.stack(reshaped_grids, axis=1)

    def calculateAmountOfSplit(self,range:Range,numberInOne:int):
        amount = int( float((range.get_max()) - float(range.get_min())) * numberInOne)
        if amount < 10:
            return 10
        return amount

    def get_axis(self,index:int):
        range = self.ranges[index]
        numberOfSplit = self.calculateAmountOfSplit(range, self.numberInOne)
        axe = numpy.linspace(range.get_min(), range.get_max(), numberOfSplit)
        return tensorflow.constant(axe, shape=(numberOfSplit, 1), dtype='float64')

    def get_axis_amount(self):
        return len(self.ranges)

    def __str__(self):
        string = ""
        for range in self.ranges:
            string += f"{range},"

        return f'[{string}]'