"""Runs unit tests on Players

This should be run by running unittesting.py in the main foldor
or the imports will fail.
"""
import unittest
from player import Player
from point_of_interest import PointOfInterest


class PlayerTests(unittest.TestCase):
    """Tests whether the Player class is working"""

    def setUp(self):
        self.player = Player("Test")
        self.point = PointOfInterest("Test")

    def test_default(self):
        self.assertEqual(self.player.name, "Test")

    def test_addPoint(self):
        self.player.addPointOfInterest(self.point)

    def test_addDuplicate(self):
        self.player.addPointOfInterest(self.point)
        with self.assertRaises(AttributeError):
            self.player.addPointOfInterest(self.point)

    def test_addSameName(self):
        pointTwo = PointOfInterest("Test", 'epic', True)
        self.player.addPointOfInterest(self.point)
        with self.assertRaises(AttributeError):
            self.player.addPointOfInterest(pointTwo)

    def test_getPoint(self):
        self.player.addPointOfInterest(self.point)
        pointTwo = self.player.getPointOfInterest("Test")
        self.assertIsInstance(pointTwo, PointOfInterest)
        self.assertEqual(self.point, pointTwo)

    def test_getPointWithObject(self):
        self.player.addPointOfInterest(self.point)
        pointTwo = self.player.getPointOfInterest(self.point)
        self.assertEqual(self.point, self.pointTwo)

    def test_removePoint(self):
        self.player.addPointOfInterest(self.point)
        self.player.removePointOfInterest(self.point.name)
        self.assertIsNone(self.player.getPointOfInterest(self.point.name))

    def test_removePointWithObject(self):
        self.player.addPointOfInterest(self.point)
        self.player.removePointOfInterest(self.point)
        self.assertIsNone(self.player.getPointOfInterest(self.point))

    def test_markSolved(self):
        if self.point.solved:
            self.point.markUnsolved()
        self.player.addPointOfInterest(self.point)
        self.player.markSolved(self.point.name)
        pointTwo = self.player.getPointOfInterest(self.point.name)
        self.assertFalse(self.point.solved)
        self.assertTrue(pointTwo.solved)

    def test_markeSolvedWithObject(self):
        if self.point.solved:
            self.point.markUnsolved()
        self.player.addPointOfInterest(self.point)
        self.player.markSolved(self.point)
        pointTwo = self.player.getPointOfInterest(self.point)
        self.assertFalse(self.point.solved)
        self.assertTrue(pointTwo.solved)

    def test_markUnsolved
