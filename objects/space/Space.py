import numpy
import tensorflow

class Space:
    def __init__(self, points:[numpy.ndarray]):
        if points is None:
            raise ValueError('points cannot be None')
        if len(points) == 0:
            raise ValueError("No points is empty")
        if points[0].ndim != 1:
            raise ValueError('points must be a 1-dimensional array')

        self.__points = points

    def get_numpy_array(self,index:int):
        return self.__points[index]

    def get_dimension(self):
        return len(self.__points)

    def get_tensorflow_array(self):
        axes_array = []

        for axe in self.__points:
            axe = tensorflow.constant(axe, shape=(len(axe), 1), dtype='float64')
            axes_array.append(axe[:, 0])

        mesh_grids = tensorflow.meshgrid(*axes_array, indexing='ij')

        reshaped_grids = [tensorflow.reshape(grid, [-1]) for grid in mesh_grids]
        return tensorflow.stack(reshaped_grids, axis=1)

    def __get_axe_length(self,axe:numpy.ndarray):
        return len(axe)