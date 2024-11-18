from functions.SimpleFunction import SimpleFunction
from solvers.AiSolver import AiSolver
from objects.Space import Space
from functions.loss.LossFunction import LossFunction

class SolutionFunction(SimpleFunction):
    def __init__(self,variables: Space,loss_function:LossFunction,learning_rate:float):
        self.ai_solver = AiSolver(variables,self,loss_function,learning_rate)

    def calculate_as_numpy(self, x):
        pass

    def calculate_as_tensor_flow(self, x):
        return self.calculate(x)

    def calculate(self, x):
        return x*self.ai_solver.calculate(x)