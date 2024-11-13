class Number:

    def __init__(self, number: float):
        self.number = number

    def get_float(self):
        return self.number

    def __eq__(self, other):
        return self.number == other.number

    def __lt__(self, other):
        return self.number < other.number

    def __gt__(self, other):
        return self.number > other.number

    def __str__(self):
        return str(self.number)

    def __int__(self):
        return int(self.number)

    def __float__(self):
        return float(self.number)
