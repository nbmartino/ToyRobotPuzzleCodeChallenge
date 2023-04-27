from directionservice import DirectionService
from toyrobot import ToyRobot
from constants import DirectionConstants
from directionservice import DirectionService

class Command(object):
    def __init__(self):
        super(Command, self).__init__()
        self.Name = ""
        self.ArgsPattern = ""

    def Execute(self, toyRobot: ToyRobot ,args: list) -> None:
        pass

class PlaceCommand(Command, DirectionService):
    def __init__(self):
        super(PlaceCommand, self).__init__()
        self.Name = "PLACE"
        self.ArgsPattern = ArgsPattern = "^(\\d+),(\\d+),({}|{}|{}|{})$".format(DirectionConstants.NORTH.value, DirectionConstants.EAST.value, DirectionConstants.SOUTH.value, DirectionConstants.WEST.value)

    def Execute(self, toyRobot: ToyRobot , args: list) -> None:

        if len(args) < 4:
            ("Incomplete args")
            return
        
        x = int(args[1])
        y = int(args[2])
        
        if (not self.IsCoordinateWithinBoard(x)) or (not self.IsCoordinateWithinBoard(y)):
            print("ERROR: Coordinate(s) not within board ({},{}) are outside of the board".format(args[1], args[2]))
            return
        
        dir = self.GetDirectionObj(args[3])
        if dir is None:
            print("ERROR: Direction [{}] not recognized".format(args[3]))
            return
        
        toyRobot.GoTo(x, y, dir)

    def IsCoordinateWithinBoard(self,c: int):

        boundary = self.GetBoundary()
        
        return (c <= boundary.high) and (c >= boundary.low)

class MoveCommand(Command):
    def __init__(self):
        super(MoveCommand, self).__init__()
        self.name = "MOVE"

    def Execute(self, toyRobot: ToyRobot , args: list) -> None:
        toyRobot.Move()

class LeftCommand(Command):
    def __init__(self):
        super(LeftCommand, self).__init__()
        self.name = "LEFT"

    def Execute(self, toyRobot: ToyRobot , args: list) -> None:
        toyRobot.RotateLeft()

class RightCommand(Command):
    def __init__(self):
        super(RightCommand, self).__init__()
        self.name = "RIGHT"

    def Execute(self, toyRobot: ToyRobot , args: list) -> None:
        toyRobot.RotateRight()

class ReportCommand(Command):
    def __init__(self):
        super(ReportCommand, self).__init__()
        self.name = "REPORT"

    def Execute(self, toyRobot: ToyRobot , args: list) -> None:
        toyRobot.Report()