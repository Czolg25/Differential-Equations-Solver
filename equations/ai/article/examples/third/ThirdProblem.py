from objects.Equation import *


class ThirdProblem(Equation):
    def __init__(self,solution:AISolution):
        super().__init__(solution, ExactSolution(),"d^2f(x)/d^2x + 1/5 * df(x)/dx + f(x) = - 1/5 * e^-(x/5) * cos(x); f(0) = 0, f(1) = sin(1) * e^-(1/5)")


class Loss(LossFunction):
    def _left_side_of_the_equation(self, function, *x):
        with tensorflow.GradientTape() as g:
            for point in x:
                g.watch(point)
            y = function(*x)

        x = x[0]
        differential = g.gradient(y, x)
        if differential is None:
            differential = tensorflow.zeros_like(x)

        return differential + y / 5

    def _right_side_of_the_equation(self, function, *x):
        x = x[0]
        return numpy.exp(-x / 5) * numpy.cos(x)

class ExactSolution(Function):
    def calculate(self, *vars):
        x = vars[0]
        return tensorflow.exp(-x/5)*tensorflow.sin(x)