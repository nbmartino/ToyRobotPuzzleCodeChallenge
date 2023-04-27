import sys, os
from commandinvoker import CommandInvoker
from toyrobot import ToyRobot
from utils import FileParser

def main():

    fileName = "default.txt"
    
    if len(sys.argv) > 1 :
        fileName = sys.argv[1]

    filePath = os.path.dirname(__file__)
    filePath = os.path.join(filePath, fileName)

    cmdInvoker = CommandInvoker()
    fileParser =  FileParser()
    toyRobot = ToyRobot()

    for line in fileParser.ParseLinesIntoList(filePath):
        if line and not line.isspace():
            cmdInvoker.ExecuteCommand(toyRobot, line)
        else:
            toyRobot.Reset()
            print("")

if __name__ == "__main__":
    main()