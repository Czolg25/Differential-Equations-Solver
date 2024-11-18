from objects.Variables import Variables
from plots.Plot3d import Plot3d
from plots.Plot2d import Plot2d
from functions.SimpleFunction import SimpleFunction
import tensorflow

class Plot:
    '''
    labels is string array
    title is string
    '''
    def __init__(self,variables:Variables,labels,title,function:SimpleFunction):
        self.variables = variables
        self.labels = labels
        self.title = title
        self.function = function;

    def choose(self):
        vars = []
        for i in range(self.variables.size()):
            vars.append(self.variables.get_variable_as_numpy(i))

        add_number = 1
        vars_number = (self.variables.size() + add_number)

        if vars_number == 2:
            return Plot2d(vars,self.labels,self.title,self.function)
        if vars_number == 3:
            return Plot3d(vars,self.labels,self.title,self.function)

        raise ValueError("Dimention not fount")
