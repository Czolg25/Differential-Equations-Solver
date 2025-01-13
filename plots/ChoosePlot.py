from plots.Plot2d import Plot2D
import numpy


class ChoosePlot:
    def __init__(self,x,y,z = None):
        if x is None:
            raise ValueError("x cannot be None")
        if y is None:
            raise ValueError("y cannot be None")

        self.__x = numpy.array(x) if not isinstance(x, numpy.ndarray) else x
        self.__y = numpy.array(y) if not isinstance(y, numpy.ndarray) else y
        self.__z = numpy.array(z) if z is not None and not isinstance(z, numpy.ndarray) else z

    def choose(self):
        if self.__z is None:
            pass
        return Plot2D(self.__x,self.__y)
