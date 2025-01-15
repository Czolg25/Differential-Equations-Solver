from objects.Range import Range
from objects.space.SpaceRanges import SpaceRanges
from plots.ChoosePlot import ChoosePlot
from solvers.AISolver import AISolver

if __name__ == '__main__':
    s = SpaceRanges(2,Range(1,20),Range(0,19)).split()

    x = s.get_numpy_array(0)
    y = s.get_numpy_array(1)

    so = AISolver(s.get_numpy_array(0),s.get_numpy_array(1))
    so.solve(10)

    import numpy
    import tensorflow as tf

    x, y = numpy.meshgrid(x,y)
    x_flat = x.flatten().reshape(-1, 1)
    t_flat = y.flatten().reshape(-1, 1)
    z = so.u_approx(tf.constant(x_flat, dtype='float64'),
                  tf.constant(t_flat, dtype='float64')).numpy().reshape(x.shape)

    c = ChoosePlot(s,z)
    c.choose().plot()