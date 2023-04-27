from toyrobot import ToyRobot
from commandinvoker import CommandInvoker
from constants import DirectionConstants, CommandConstants
from coordinates import Coordinates
from directionservice import DirectionService
from utils import ComposePlaceCommand

directionService = DirectionService()
cmdInvoker = CommandInvoker()
toyRobot = ToyRobot()
coords = Coordinates(1, 1)

def test_toy_robot_move_facing_north():
    toyRobot.Reset()
    expectedY = coords.y + 1
    
    cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(coords.x, coords.y, DirectionConstants.NORTH.value))
    cmdInvoker.ExecuteCommand(toyRobot, CommandConstants.MOVE.value)

    assert expectedY == toyRobot.currPos.y

def test_toy_robot_move_facing_east():
    toyRobot.Reset()
    expectedX = coords.x + 1

    cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(coords.x, coords.y, DirectionConstants.EAST.value))
    cmdInvoker.ExecuteCommand(toyRobot, CommandConstants.MOVE.value)

    assert expectedX == toyRobot.currPos.x

def test_toy_robot_move_facing_south():
    toyRobot.Reset()
    expectedY = coords.y - 1

    cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(coords.x, coords.y, DirectionConstants.SOUTH.value))
    cmdInvoker.ExecuteCommand(toyRobot, CommandConstants.MOVE.value)

    assert expectedY == toyRobot.currPos.y

def test_toy_robot_move_facing_west():
    toyRobot.Reset()
    expectedX = coords.x- 1

    cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(coords.x, coords.y, DirectionConstants.WEST.value))
    cmdInvoker.ExecuteCommand(toyRobot, CommandConstants.MOVE.value)

    assert expectedX == toyRobot.currPos.x
