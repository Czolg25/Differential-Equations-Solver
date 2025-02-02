from objects.functions.Function import Function
import tensorflow
import numpy

class LossFunction(Function):
    def calculate(self, function, *x):
        y = (self._left_side_of_the_equation(function, *x) - self._right_side_of_the_equation(function, *x)
             - self._condition(function, *x))
        return tensorflow.reduce_mean(y ** 2)

    def _left_side_of_the_equation(self, function, *x):
        return 0

    def _right_side_of_the_equation(self, function, *x):
        return 0

    def _condition(self, function, *x):
        return 0
