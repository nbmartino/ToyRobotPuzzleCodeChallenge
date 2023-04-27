from direction import Direction
from coordinates import Coordinates

class ToyRobot:

    def __init__(self) -> None:
        self.currPos = Coordinates()
        self.currDir: Direction = None

    def IsPlacedOnBoard(self) -> bool:
        return self.currDir != None

    def GoTo(self, x: int, y: int , direction: Direction ):
        self.currPos.x = x
        self.currPos.y = y
        self.currDir = direction

    def Move(self):
        self.currDir.move(self.currPos)

    def Report(self):
        print("{},{},{}".format(self.currPos.x, self.currPos.y, self.currDir.name))

    def Reset(self):
        self.currPos.x = -1
        self.currPos.y = -1
        self.currDir = None

    def RotateLeft(self):
        self.currDir = self.currDir.left

    def RotateRight(self):
        self.currDir = self.currDir.right
