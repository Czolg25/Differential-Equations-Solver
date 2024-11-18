import matplotlib.pyplot as plot
import numpy
from functions.SimpleFunction import SimpleFunction

class Plot3d:

    '''
    variables - type of numpy array
    labels is string array

    '''
    def __init__(self,variables,labels,title,function:SimpleFunction):
        if (len(variables) + 1) != len(labels):
            raise ValueError("length of labels does not equal to length of variables")

        self.variables = variables
        self.labels = labels
        self.title = title
        self.function = function

    def show(self):
        fig = plot.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')

        x,y = numpy.meshgrid(self.variables[0],self.variables[1])
        z = self.function.calculate_as_tensor_flow([x,y])
        ax.plot_surface(x,y,z,
                        cmap='viridis', edgecolor='k', alpha=0.8)

        ax.set_xlabel(self.labels[0])
        ax.set_ylabel(self.labels[1])
        ax.set_zlabel(self.labels[2])

        ax.set_title(self.title)

        plot.show()
