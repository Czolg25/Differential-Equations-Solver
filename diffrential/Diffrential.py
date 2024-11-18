import tensorflow
from objects.Space import Space


class Differential:
    def calculate(self,function, space: Space, *diffrentials: int):
        y = None

        with tensorflow.GradientTape(persistent=True) as tape:
            axes = [space.get_axis(i) for i in range(space.get_axis_amount())]
            for axis in axes:
                tape.watch(axis)

            y = function(axes)

            for diffrential in diffrentials:
                dx = tape.gradient(y, axes)
                dx = [tensorflow.zeros_like(axis) if grad is None else grad for axis, grad in zip(axes, dx)]

                y = dx[diffrential]

        del tape

        return y
