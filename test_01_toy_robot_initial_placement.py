from toyrobot import ToyRobot
from commandinvoker import CommandInvoker
from constants import DirectionConstants, CommandConstants
from directionservice import DirectionService
from utils import ComposePlaceCommand


def test_placed_at_a_valid_position_facing_a_valid_direction():
    toyRobot = ToyRobot()
    cmdInvoker = CommandInvoker()
    dirs = [DirectionConstants.NORTH.value, DirectionConstants.EAST.value, DirectionConstants.SOUTH.value, DirectionConstants.WEST.value]
    x = 0
    y = 0
    
    for dir in dirs:

        cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(x, x, dir))

        assert dir == toyRobot.currDir.name
        assert x == toyRobot.currPos.x
        assert y == toyRobot.currPos.y

def test_not_placed_when_direction_is_invalid():
    toyRobot = ToyRobot()
    cmdInvoker = CommandInvoker()
    x = 0
    y = 0

    cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(x, y, "NORTHFACE")) 

    assert False == toyRobot.IsPlacedOnBoard()

def test_not_placed_outside_the_board():
    toyRobot = ToyRobot()
    cmdInvoker = CommandInvoker()
    dirSvc =  DirectionService()
    boundary = dirSvc.GetBoundary()
    x = 0
    y = 0

    cmdInvoker.ExecuteCommand(toyRobot, ComposePlaceCommand(boundary.low - 1, boundary.high + 1, DirectionConstants.NORTH.value))

    assert False == toyRobot.IsPlacedOnBoard()

def test_other_commands_are_ignored_until_the_robot_is_placed():
    toyRobot = ToyRobot()
    cmdInvoker = CommandInvoker()
    x = toyRobot.currPos.x
    y = toyRobot.currPos.y

    cmdInvoker.ExecuteCommand(toyRobot,CommandConstants.MOVE.value)
    assert x == toyRobot.currPos.x
    assert y == toyRobot.currPos.y

    cmdInvoker.ExecuteCommand(toyRobot,CommandConstants.REPORT.value)

    cmdInvoker.ExecuteCommand(toyRobot,CommandConstants.LEFT.value)
    assert toyRobot.currDir is None

    cmdInvoker.ExecuteCommand(toyRobot,CommandConstants.RIGHT.value)
    assert toyRobot.currDir is None

