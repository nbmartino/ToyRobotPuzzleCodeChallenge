
def ComposePlaceCommand(x: int, y: int, dir: str) -> str:
    return "PLACE {},{},{}".format(str(x), str(y), dir)

class FileParser:
    def ParseLinesIntoList(self, filename: str) -> list:
        self.lines: list = []
        cmdFile = open( filename, 'r')
        return cmdFile.readlines()
