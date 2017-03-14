"""Holds the PointOfInterest class and the InvalidPoint exception"""


class PointOfInterest:
    """Contains all of the information of an Eleuthia Point of Interest

    Valid difficulties are: 'unknown', 'normal', 'epic', 'deadly',
                            and 'forbidden'

    Public attributes: name, difficulty, and solved
    """

    difficulties = {'unknown', 'normal', 'epic', 'deadly', 'forbidden'}

    def __init__(self, name, difficulty="unknown", solved=False):
        """Constructs a Point of Interest.

        It is given the difficulty 'unknown' and marked as unsolved if those
        are not specificed.

        Trying to create a Point of Interest with an invalid difficulty
        raises a TypeError.
        """
        if difficulty not in self.difficulties:
            raise TypeError("{0} is not a valid difficulty".format
                            (difficulty))
        self.name = name
        self.difficulty = difficulty
        self.solved = solved

    def changeName(self, name):
        """Changes the name of a Point of Interest"""
        self.name = name

    def markSolved(self):
        """Marks a Point of Interest as solved.

        Marking a solved point as solved raises AttributeError."""
        if self.solved:
            raise AttributeError("Point of Interest is already solved")
        self.solved = True

    def markUnsolved(self):
        """Marks a Point of Interest as unsolved.

        Marking an unsolved point as unsolved raises AttributeError."""
        if not self.solved:
            raise AttributeError("Point of Interest is already solved")
        self.solved = False

    def changeDifficulty(self, difficulty):
        """Changes the difficulty of the Point of Interest.

        Changing the difficulty to an invalid difficulty raises a TypeError."""
        if difficulty not in self.difficulties:
            raise TypeError("{0} is not a valid difficulty".format
                            (difficulty))
        self.difficulty = difficulty
