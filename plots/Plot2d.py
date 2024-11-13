import matplotlib.pyplot as plot
import numpy

class Plot2d:

    '''
    variables - type of numpy array
    labels is string array

    '''
    def __init__(self,variables,labels,title,function):
        if (len(variables) + 1) != len(labels):
            raise ValueError("length of labels does not equal to length of variables")

        self.variables = variables
        self.labels = labels
        self.title = title
        self.function = function

    def show(self):
        x = numpy.meshgrid(self.variables[0])
        y = self.function(x)

        plot.plot(x, y, label=self.title, color='blue', marker='o')

        plot.title(self.title)
        plot.xlabel(self.labels[0])
        plot.ylabel(self.labels[1])

        plot.show()
