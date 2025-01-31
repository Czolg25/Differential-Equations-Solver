from abc import abstractmethod

from objects.space.Space import Space


class Function:
    def calculate_as_numpy(self,space:Space):
        points = space.get_points()
        result = self._calculate(*points)
        return result.numpy().reshape(space.get_shape())

    @abstractmethod
    def _calculate(self,*vars):
        pass