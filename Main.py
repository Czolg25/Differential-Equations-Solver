from objects.Space import Space
from objects.Range import Range
from objects.Variables import Variables
from plots.Plot import Plot

import numpy as np

def f(x):
    return tensorflow.pow(x,2)

import tensorflow

if __name__ == '__main__':

    space = Space(Range(-10,10))
    points = space.split(10)

    vars = Variables(points)
    plot = Plot(vars,["a","b"],"ss",points)
    p = plot.choose()
    p.show()

