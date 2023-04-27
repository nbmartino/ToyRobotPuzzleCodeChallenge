class Direction:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.left: Direction = None
        self.right: Direction = None
        self.move: function = None
