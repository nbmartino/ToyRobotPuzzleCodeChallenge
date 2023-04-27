from boundary import Boundary
from direction import Direction
from constants import DirectionConstants
from coordinates import Coordinates
class DirectionService(object):
     
    boundary = Boundary(0, 4)
    directions = {}

    def __init__(self)-> None:
        super(DirectionService, self).__init__()
        self.InitializeDirections()
    
    def GetDirectionObj(self, dir: str) -> Direction:
        return DirectionService.directions.get(dir)

    def GetBoundary(self) -> Boundary:
        return DirectionService.boundary
    
    def NorthMove(self, c: Coordinates):
        if c.y != self.GetBoundary().high :
            c.y += 1

    def EastMove(self, c: Coordinates):
        if c.x != self.GetBoundary().high :
            c.x += 1

    def SouthMove(self, c: Coordinates):
        if c.y != self.GetBoundary().low :
            c.y -= 1

    def WestMove(self, c: Coordinates):
        if c.x != self.GetBoundary().low :
            c.x -= 1

    def InitializeDirections(self):
        DirectionService.directions[DirectionConstants.NORTH.value] = Direction(DirectionConstants.NORTH.value)
        DirectionService.directions[DirectionConstants.EAST.value] = Direction(DirectionConstants.EAST.value)
        DirectionService.directions[DirectionConstants.SOUTH.value] = Direction(DirectionConstants.SOUTH.value)
        DirectionService.directions[DirectionConstants.WEST.value] = Direction(DirectionConstants.WEST.value)
        
        # Link adjacent directions
        DirectionService.directions[DirectionConstants.NORTH.value].left = DirectionService.directions[DirectionConstants.WEST.value]
        DirectionService.directions[DirectionConstants.NORTH.value].right = DirectionService.directions[DirectionConstants.EAST.value]

        DirectionService.directions[DirectionConstants.EAST.value].left = DirectionService.directions[DirectionConstants.NORTH.value]
        DirectionService.directions[DirectionConstants.EAST.value].right = DirectionService.directions[DirectionConstants.SOUTH.value]

        DirectionService.directions[DirectionConstants.SOUTH.value].left = DirectionService.directions[DirectionConstants.EAST.value]
        DirectionService.directions[DirectionConstants.SOUTH.value].right = DirectionService.directions[DirectionConstants.WEST.value]

        DirectionService.directions[DirectionConstants.WEST.value].left = DirectionService.directions[DirectionConstants.SOUTH.value]
        DirectionService.directions[DirectionConstants.WEST.value].right = DirectionService.directions[DirectionConstants.NORTH.value]

        # Assign move functions
        DirectionService.directions[DirectionConstants.NORTH.value].move = self.NorthMove
        DirectionService.directions[DirectionConstants.EAST.value].move = self.EastMove
        DirectionService.directions[DirectionConstants.SOUTH.value].move = self.SouthMove
        DirectionService.directions[DirectionConstants.WEST.value].move = self.WestMove