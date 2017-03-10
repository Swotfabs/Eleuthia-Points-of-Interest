"""Holds the PointOfInterest class and the InvalidPoint exception"""

class InvalidPointException(Exception):
    """This exception is thrown when an invalid point of interest is created"""

    pass

class PointOfInterest:
    """Contains all of the information of an Eleuthia Point of Interest

    Has the grades: 'unknown', 'normal', 'epic', 'deadly', and 'forbidden'
    """

    self.grades = {'unknown', 'normal', 'epic', 'deadly', 'forgidden'}

    def __init__ (self, name, grade="unknown", solved=False)
        """Constructs a Point of Interest.

        It is given the grade 'unknown' and marked as unsolved if those are
        not specificed
        """
        assert False, "Not Yet Implemented"
