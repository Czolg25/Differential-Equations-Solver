from objects.tasks.TaskEquationData import TaskEquationData
from objects.Range import Range
from objects.Space import Space
from functions.loss.LossFunction import LossFunction
from functions.SimpleFunction import SimpleFunction

import numpy


class SimpleEquation(TaskEquationData):
    def __init__(self):
        super().__init__( Space(10, Range(0, 1) ), SimpleLoss(),"y'=y y(0)=1",
                         ["x","y(x)"],ExactSolution())

class SimpleLoss(LossFunction):
    def calculate(self, function, space: Space):
        return self.diff.calculate(function, space, 0) - function(space.split()) - 1

class ExactSolution(SimpleFunction):

    def calculate(self, x):
        return numpy.exp(x)