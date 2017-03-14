"""Holds the Player class which has points of interest"""


class Player:
    """Contains Points of Interest belonging to the player in sorted containers

    Public attributes: name
    """

    def __init__(self, name):
        """Creates a Player"""
        assert False, "Not Yet Implemented"

    def addPointOfInterest(self, point):
        """Adds a copy of a Point of Interest to the player.

        Raises a AttributeError if the player already has a Point of Interest
            by the same name.
        """
        assert False, "Not Yet Implemented"

    def getPointOfInterest(self, point):
        """Returns a point of Interest belonging to the player but
            does not remove it.

        Returns None if no Point of Interest by that name is found.
        """
        assert False, "Not Yet Implemented"

    def removePointOfInterest(self, point):
        """Removes a point of interest from the player."""

        assert False, "Not Yet Implemented"

    def markSolved(self, point):
        """Marks a Point of Interest as solved."""

        assert False, "Not Yet Implemented"

    def markUnsolved(self, point):
        """Marks a Point of Interest as unsolved."""

        assert False, "Not Yet Implemented"

    def changeDifficulty(self, point, difficulty):
        """Changes the difficulty of a Point of Interest."""

        assert False, "Not Yet Implemented"

    def solvedPoints(self):
        """A generator for solved points of interest.

        Points of Interest yielded will be sorted alphabetically by
        their title.
        """

        assert False, "Not Yet Implemented"

    def unsolvedPoints(self):
        """A generator for unsolved points of interest.

        Points of Interest yielded will be sorted alphabetically by
        their title.
        """

        assert False, "Not Yet Implemented"
