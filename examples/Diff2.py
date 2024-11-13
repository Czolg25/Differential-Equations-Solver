import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from objects.Space import Space
from objects.Range import Range
from objects.Variables import Variables
from plots.Plot import Plot

from plots.Plot import Plot
from objects.Variables import Variables

# Definiujemy funkcję f(x) = x^2
def f(x):
    return np.pow(x,2)
def f2(x):
    return x[0]**2;

# Tworzymy zmienne TensorFlow
space = Space(Range(-10,10),Range(-5,5))
x = space.split(10)


def diff(power:int,function,vars):
    y = []
    # Używamy gradient tape, aby obliczyć pochodne
    with tf.GradientTape(persistent=True) as tape:
        for x in vars:
            tape.watch(x)

        print(vars)
        y.append(function(vars))
        print(y)

        for i in range(power):
            y2 = []
            dy_dx = tape.gradient(y[len(y) - 1],vars)
            #y2.append(dy_dx)
            y.append(dy_dx)
    del tape
    return y

print(x[1])
print(diff(3,f2,x[0])[0])
