from objects.Number import Number


class Range:

    def __init__(self, min, max):
        self.__init__(Number(min), Number(max))

    def __init__(self, min: Number, max: Number):
        if min >= max:
            raise ValueError("Min must be less than or equal to max")

        self.min = min
        self.max = max

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def __str__(self):
        return f'<{self.min};{self.max}>'
