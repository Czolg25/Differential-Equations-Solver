from objects.Range import Range
from objects.space.SpaceRanges import SpaceRanges
from plots.ChoosePlot import ChoosePlot
from solvers.AISolver import AISolver


from objects.functions.Funtion import Function

class D(Function):

    def _calculate(self,*vars):
        return vars[0]

if __name__ == '__main__':
    s = SpaceRanges(2,Range(-1,1),Range(-1,1)).split()

    so = AISolver(s.get_numpy_array(0),s.get_numpy_array(1))
    so.solve(10)

    z = D().calculate_as_numpy(s)

    c = ChoosePlot(s,z)
    c.choose().plot()