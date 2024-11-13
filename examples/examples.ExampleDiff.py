import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from objects.Space import Space
from objects.Range import Range
from objects.Variables import Variables
from plots.Plot import Plot


# Definiujemy funkcję
def f(x):
    return x**2

# Tworzymy zmienne TensorFlow
x = tf.Variable(initial_value=np.linspace(-10, 10, 100), dtype=tf.float32)

# Używamy gradient tape, aby obliczyć pochodną
with tf.GradientTape() as tape:
    y = f(x)

# Obliczamy pochodną
dy_dx = tape.gradient(y, x)

# Konwertujemy dane na numpy dla łatwego rysowania
x_vals = x.numpy()
y_vals = y.numpy()
dy_dx_vals = dy_dx.numpy()

# Wykres funkcji i jej pochodnej
plt.figure(figsize=(10, 6))

plt.plot(x_vals, y_vals, label="f(x) = x^2", color="blue")
plt.plot(x_vals, dy_dx_vals, label="f'(x) = 2x", color="red", linestyle="dashed")

plt.title("Wykres funkcji f(x) = x^2 oraz jej pochodnej")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
