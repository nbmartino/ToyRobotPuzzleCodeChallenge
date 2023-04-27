# ToyRobotPuzzleCodeChallenge

Toy Robot Code Challenge

The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.

Create a console application that can read in commands of the following form -

PLACE X,Y,F will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST

MOVE will move the toy robot one unit forward in the direction it is currently facing

LEFT will rotate the robot 90 degrees in the specified direction without changing the position of the robot

RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

REPORT will announce the X,Y and F of the robot


HOW TO RUN:

1. Run commands from a file - go to source folder in a terminal, type in 'python3 main.py commands.txt' then press [enter]

2. Run test - go to source folder in a terminal, type in 'pytest -s' then press [enter]
