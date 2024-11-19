import numpy
import tensorflow

class SimpleFunction:

    def calculate_as_numpy(self, x):
        pass

    def calculate_as_tensor_flow(self, x):
        return self.calculate(x)

    def calculate(self, x):
        pass