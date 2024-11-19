from objects.tasks.TaskEquationData import TaskEquationData
from objects.Range import Range
from objects.Space import Space
from functions.loss.LossFunction import LossFunction
from functions.SimpleFunction import SimpleFunction
import tensorflow

import numpy
class Part(TaskEquationData):
    def __init__(self):
        super().__init__( Space(10, Range(0, 1),Range(0, 1) ), SimpleLoss(),"y''+y=x y(0) = 2, y'(0)=1",
                         ["x","y(x)"],ExactSolution())

class SimpleLoss(LossFunction):

    def calculate(self, function, space: Space):
        x,y = space.get_axis(0), space.get_axis(1)
        return (self.diff.calculate(function,space,0,0)+self.diff.calculate(function,space,1,1)-tensorflow.sin(x*y))

class ExactSolution(SimpleFunction):

    def calculate(self, x):
        return x[0]**2+x[1]**2