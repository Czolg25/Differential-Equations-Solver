import matplotlib.pyplot as plot
import numpy
import tensorflow
from functions.SimpleFunction import SimpleFunction

class Plot2d:

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
        x = tensorflow.transpose(tensorflow.convert_to_tensor(numpy.meshgrid(self.variables[0])))

        y = self.function.calculate_as_tensor_flow(x)

        plot.plot(x, y, label=self.title, color='black')

        plot.title(self.title)
        plot.xlabel(self.labels[0])
        plot.ylabel(self.labels[1])

        plot.show()
