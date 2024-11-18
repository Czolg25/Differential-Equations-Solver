from objects.Space import Space
from functions.loss import LossFunction


class TaskEquationData:
    def __init__(self, space: Space, loss_function: LossFunction, function_name: str, labels):
        self.space = space
        self.loss_function = loss_function
        self.function_name = function_name
        self.labels = labels

    def get_space(self):
        return self.space

    def get_loss_function(self):
        return self.loss_function

    def get_function_name(self):
        return self.function_name

    def get_labels(self):
        return self.labels
