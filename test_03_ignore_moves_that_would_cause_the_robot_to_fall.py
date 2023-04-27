from toyrobot import ToyRobot
from commandinvoker import CommandInvoker
from constants import DirectionConstants, CommandConstants
from coordinates import Coordinates
from directionservice import DirectionService
from utils import ComposePlaceCommand

directionService = DirectionService()
cmdInvoker = CommandInvoker()
toyRobot = ToyRobot()

def  test_invalid_move_past_x_high_boundary():
    coords = Coordinates(4, 4)
    expectedX = coords.x

    cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(coords.x, coords.y, DirectionConstants.EAST.value))
    cmdInvoker.ExecuteCommand(toyRobot, CommandConstants.MOVE.value)

    assert expectedX == toyRobot.currPos.x

def test_invalid_move_past_y_high_boundary():
    coords = Coordinates(4, 4)
    expectedY = coords.y

    cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(coords.x, coords.y, DirectionConstants.NORTH.value))
    cmdInvoker.ExecuteCommand(toyRobot, CommandConstants.MOVE.value)

    assert expectedY == toyRobot.currPos.y

def  test_invalid_move_past_x_low_boundary():
    coords = Coordinates(0, 0)
    expectedX = coords.x

    cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(coords.x, coords.y, DirectionConstants.WEST.value))
    cmdInvoker.ExecuteCommand(toyRobot, CommandConstants.MOVE.value)

    assert expectedX == toyRobot.currPos.x

def test_invalid_move_past_y_low_boundary():
    coords = Coordinates(0, 0)
    expectedY = coords.y

    cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(coords.x, coords.y, DirectionConstants.SOUTH.value))
    cmdInvoker.ExecuteCommand(toyRobot, CommandConstants.MOVE.value)

    assert expectedY == toyRobot.currPos.y