from objects.space.Space import Space
from objects.plot.PlotData import PlotData
from plots.Plot2d import Plot2D
from plots.Plot3d import Plot3D

import matplotlib

matplotlib.use('TkAgg')


class ChoosePlot:
    def __init__(self, space: Space, plot_data: PlotData = PlotData()):
        if space is None:
            raise ValueError("Space cannot be None")

        self.__space = space
        self.__plot_data = plot_data

    def choose(self):
        dimension = self.__space.get_dimension()
        if dimension == 2:
            return Plot2D(self.__space.get_numpy_array(0), self.__space.get_numpy_array(1), self.__plot_data)
        elif dimension == 3:
            return Plot3D(self.__space.get_numpy_array(0), self.__space.get_numpy_array(1), self.__space.get_numpy_array(2), self.__plot_data)
        else:
            raise ValueError("Dimension not supported")
