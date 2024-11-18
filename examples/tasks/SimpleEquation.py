from objects.tasks.TaskEquationData import TaskEquationData
from objects.Range import Range
from objects.Space import Space
from functions.loss import LossFunction


class SimpleEquation(TaskEquationData):
    def __init__(self):
        super().__init__(Space(100, Range(-1, 1)), SimpleLoss(),"y'=y y(0)=1",
                         ["x","y(x)"])


class SimpleLoss(LossFunction):
    def calculate(self, function, space: Space):
        return self.diff.calculate(function, space, 0) - function(space.split()) - 1
