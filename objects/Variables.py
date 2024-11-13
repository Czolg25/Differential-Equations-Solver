import tensorflow
import numpy

class Variables:

    '''
    variables type is tensor array
    '''
    def __init__(self,variables):
        if variables is None or len(variables)==0:
            raise ValueError('Variables cannot be empty')


        tempVariables = []
        for var in variables[0]:
            tempVariables.append([])

        for variable in variables:
            if len(variable) != len(variables[0]):
                raise ValueError('Variables must have same length')
            if not isinstance(variable, tensorflow.Tensor):
                raise ValueError("Variables must have type tensorflow.Tensor")
            for i in range(len(variable)):
                tempVariables[i].append(variable[i])

        for i in range(len(tempVariables)):
            tempVariables[i] = tensorflow.convert_to_tensor(tempVariables[i])
        self.variables = tempVariables

    def get_variable_as_tensorflow_tensor(self,index:int):
        return self.variables[index]
    def get_variable_as_numpy(self,index:int):
        return self.variables[index].numpy()

    def size(self):
        return len(self.variables)

    def __str__(self):
        return str(self.variables)