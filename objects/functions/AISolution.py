from solvers.AISolver import AISolver
from objects.functions.Function import *
from objects.functions.loss.LossFunction import LossFunction
from objects.space.Space import Space

class AISolution(Function):
    def __init__(self,space:Space,loss_function:LossFunction):
        self._ai_solver = AISolver(space,self.calculate,loss_function)

    def calculate(self,*vars):
        return self._ai_solver.calculate(*vars)

    def solve(self,epochs:int):
        return self._ai_solver.solve(epochs)