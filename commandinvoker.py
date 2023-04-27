import re
from commands import Command
from commands import PlaceCommand, MoveCommand, LeftCommand, RightCommand, ReportCommand
from constants import CommandConstants
from fileparser import FileParser
from mylogging import Logger
from toyrobot import ToyRobot

class CommandInvoker:

    def __init__(self) -> None:
        self.parser = FileParser()
        self.commandMap = {}
        self.cmdList = ""
        self.InitializeCommandMap()
        self.BuildCommandListString()
        self.cmdPattern = "^(" + self.cmdList + ")\\s?(.*)"

    def ExecuteCommand(self, toyRobot: ToyRobot, inStr: str) -> None:

        if len(inStr) < 1:
            return
        
        cmdStr = inStr.strip().upper()
        parsedCmd = self.ExtractCommandAndArgs(cmdStr, self.cmdPattern)
        if Logger.DEBUG:
            for item in parsedCmd:
                Logger.log("parsedCmd: " + item)

        if len(parsedCmd) < 2:
            print("ERROR: Command string [{}] is not parsed, see if the command keyword is registered.".format(cmdStr))
            return
        
        cmd: Command = self.commandMap.get(parsedCmd[1])
        if cmd is None:
            print("ERROR: cmd is None")
            return
        
        if not self.CanExecuteCommand(cmd, toyRobot.IsPlacedOnBoard(), parsedCmd[1]):
            print("ERROR: Can not execute command")
            return
        
        args = self.ExtractArgs(parsedCmd[2], cmd.ArgsPattern)
        if Logger.DEBUG:
            if args is not None:
                for item in parsedCmd:
                    Logger.log(item)
            else:
                Logger.log("args in None")

        cmd.Execute(toyRobot, args)

    def BuildCommandListString(self) -> None:
        for k in self.commandMap:
            self.cmdList = self.cmdList + "{}|".format(k)
        self.cmdList =  self.cmdList.rstrip('|')

    def InitializeCommandMap(self) -> None:
        self.commandMap[CommandConstants.PLACE.value] = PlaceCommand()
        self.commandMap[CommandConstants.MOVE.value] = MoveCommand()
        self.commandMap[CommandConstants.LEFT.value] = LeftCommand()
        self.commandMap[CommandConstants.RIGHT.value] = RightCommand()
        self.commandMap[CommandConstants.REPORT.value] = ReportCommand()


    def CanExecuteCommand(self, cmdobj: Command, toyHasBeenPlaced: bool,  command: str):
        if (not toyHasBeenPlaced) and (cmdobj.Name != "PLACE"):
            print("ERROR: Ignoring command [" + command + "]. PLACE should be done first.")
            return False
        return True

    def IsValidCommand(self, command: str):
        pass

    def ExtractArgs(self, args: str, argsPattern: str) -> list:
        parsedArgs = self.GetMatches(args, argsPattern)
        return parsedArgs

    def GetMatches(self, input: str, pattern: str) -> list:
        return re.split(pattern, input)
    
    def ExtractCommandAndArgs(self, command: str, argsPattern: str) -> list:
        return self.GetMatches(command, argsPattern)
