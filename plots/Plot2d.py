import numpy
import matplotlib.pyplot as plot

from objects.plot.PlotData import PlotData


class Plot2D:
    def __init__(self, x: numpy.ndarray, y: numpy.ndarray, plot_data: PlotData):
        self.__x = x
        self.__y = y
        self.__plot_data = plot_data

    def plot(self):
        plot.plot(self.__x, self.__y, label="a", color='black')

        plot.title(self.__plot_data.get_title())
        plot.xlabel(self.__plot_data.get_label(0))
        plot.ylabel(self.__plot_data.get_label(1))

        plot.show()
