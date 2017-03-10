"""Holds the PointOfInterest class and the InvalidPoint exception"""


class InvalidPointException(Exception):
    """This exception is thrown when an invalid point of interest is created"""

    pass


class PointOfInterest:
    """Contains all of the information of an Eleuthia Point of Interest

    Has the difficulties: 'unknown', 'normal', 'epic', 'deadly',
    and 'forbidden'
    """

    self.difficulties = {'unknown', 'normal', 'epic', 'deadly', 'forgidden'}

    def __init__(self, name, difficulty="unknown", solved=False):
        """Constructs a Point of Interest.

        It is given the difficulty 'unknown' and marked as unsolved if those
        are not specificed
        """
        assert False, "Not Yet Implemented"

    def markSolved(self):
        """Marks a Point of Interest as solved"""
        assert False, "Not Yet Implemented"

    def markUnsolved(self):
        """Marks a Point of Interest as unsolved"""
        assert False, "Not Yet Implemented"

    def changeDifficulty(self, difficulty):
        """Changes the difficulty of the Point of Interest"""
        assert False, "Not Yet Implemented"
