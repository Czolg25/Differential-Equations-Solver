import numpy
import matplotlib.pyplot as plot
import matplotlib
matplotlib.use('QtAgg')

class Plot2D:
    def __init__(self,x:numpy.ndarray,y:numpy.ndarray):
        self.__x = x
        self.__y = y

    def plot(self):
        plot.plot(self.__x,self.__y , label="a", color='black')

        plot.title("a")
        plot.xlabel("self.labels[0]")
        plot.ylabel("self.labels[1]")

        plot.show()