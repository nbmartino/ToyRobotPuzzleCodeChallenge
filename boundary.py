
class Boundary:

    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high

    def GetBoundaries(self) -> tuple:
        return self.low, self.high