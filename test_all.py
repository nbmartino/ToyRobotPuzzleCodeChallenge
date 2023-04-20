from toyrobot import ToyRobot

def test_placed_at_a_valid_position_facing_a_valid_direction():
    toyRobot = ToyRobot()
    print(repr(toyRobot))
    assert toyRobot is not None
