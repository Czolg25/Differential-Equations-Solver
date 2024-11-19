from objects.Space import Space
from functions.loss import LossFunction
from functions.SimpleFunction import SimpleFunction
import numpy


class TaskEquationData:
    def __init__(self, space: Space, loss_function: LossFunction, function_name: str, labels,
                 exact_solution: SimpleFunction):
        self.space = space
        self.loss_function = loss_function
        self.function_name = function_name
        self.labels = labels
        self.exact_solution = exact_solution

    def get_space(self):
        return self.space

    def get_loss_function(self):
        return self.loss_function

    def get_function_name(self):
        return self.function_name

    def get_labels(self):
        return self.labels

    def get_error_function(self, ai_solution: SimpleFunction):
        return ErrorFunction(ai_solution, self.exact_solution)

    def get_error_abs_function(self, ai_solution: SimpleFunction):
        return ErrorFunctionAbs(ai_solution, self.exact_solution)


class ErrorFunction(SimpleFunction):
    def __init__(self, ai_solution: SimpleFunction, exact_solution: SimpleFunction):
        self.ai_solution = ai_solution
        self.exact_solution = exact_solution

    def calculate(self, x):
        return self.exact_solution.calculate(x) - self.ai_solution.calculate(x)


class ErrorFunctionAbs(SimpleFunction):
    def __init__(self, ai_solution: SimpleFunction, exact_solution: SimpleFunction):
        self.ai_solution = ai_solution
        self.exact_solution = exact_solution

    def calculate(self, x):
        exact_y = self.exact_solution.calculate(x)
        return numpy.abs(exact_y - self.ai_solution.calculate(x)) * 100 / exact_y
