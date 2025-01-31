import numpy
import matplotlib.pyplot as plot

from objects.plot.PlotData import PlotData


class Plot3D:
    def __init__(self, x: numpy.ndarray, y: numpy.ndarray,z: numpy.ndarray, plot_data: PlotData):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__plot_data = plot_data

    def plot(self):
        fig = plot.figure(dpi=150)
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.__x, self.__y, self.__z, cmap='viridis')
        ax.set_xlabel('$x$')
        ax.set_ylabel('$t$')
        ax.set_zlabel('$u(x, t)$')
        plot.title("Neural Network Solution to the Heat Equation")
        plot.show()