"""Holds the PointOfInterest class and the InvalidPoint exception"""


class PointOfInterest:
    """Contains all of the information of an Eleuthia Point of Interest

    Has the difficulties: 'unknown', 'normal', 'epic', 'deadly',
        and 'forbidden'
    """

    difficulties = {'unknown', 'normal', 'epic', 'deadly', 'forbidden'}

    def __init__(self, name, difficulty="unknown", solved=False):
        """Constructs a Point of Interest.

        It is given the difficulty 'unknown' and marked as unsolved if those
        are not specificed.

        Trying to create a Point of Interest with an invalid difficulty
        raises a TypeError.
        """
        assert False, "Not Yet Implemented"

    def markSolved(self):
        """Marks a Point of Interest as solved.

        Marking a solved point as solved raises AttributeError."""
        assert False, "Not Yet Implemented"

    def markUnsolved(self):
        """Marks a Point of Interest as unsolved.

        Marking an unsolved point as unsolved raises AttributeError."""
        assert False, "Not Yet Implemented"

    def changeDifficulty(self, difficulty):
        """Changes the difficulty of the Point of Interest.

        Changing the difficulty to an invalid difficulty raises a TypeError."""
        assert False, "Not Yet Implemented"
