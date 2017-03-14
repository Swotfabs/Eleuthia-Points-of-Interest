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
        # Testing
        self.assertEqual(self.player.name, "Test")

    def test_addPoint(self):
        # Testing
        self.player.addPointOfInterest(self.point)

    def test_addDuplicate(self):
        # Setup
        self.player.addPointOfInterest(self.point)

        # Testing
        with self.assertRaises(AttributeError):
            self.player.addPointOfInterest(self.point)

    def test_addSameName(self):
        # Setup
        pointTwo = PointOfInterest("Test", 'epic', True)
        self.player.addPointOfInterest(self.point)

        # Testing
        with self.assertRaises(AttributeError):
            self.player.addPointOfInterest(pointTwo)

    def test_getPoint(self):
        # Setup
        self.player.addPointOfInterest(self.point)

        # Testing
        pointTwo = self.player.getPointOfInterest("Test")
        self.assertIsInstance(pointTwo, PointOfInterest)
        self.assertEqual(self.point, pointTwo)

    def test_getPointWithObject(self):
        # Setup
        self.player.addPointOfInterest(self.point)

        # Testing
        pointTwo = self.player.getPointOfInterest(self.point)
        self.assertEqual(self.point, self.pointTwo)

    def test_removePoint(self):
        # Setup
        self.player.addPointOfInterest(self.point)

        # Testing
        self.player.removePointOfInterest(self.point.name)
        self.assertIsNone(self.player.getPointOfInterest(self.point.name))

    def test_removePointWithObject(self):
        # Setup
        self.player.addPointOfInterest(self.point)

        # Testing
        self.player.removePointOfInterest(self.point)
        self.assertIsNone(self.player.getPointOfInterest(self.point))

    def test_markSolved(self):
        # Setup
        if self.point.solved:
            self.point.markUnsolved()
        self.player.addPointOfInterest(self.point)

        # Testing
        self.player.markSolved(self.point.name)
        pointTwo = self.player.getPointOfInterest(self.point.name)
        self.assertTrue(self.point.solved)
        self.assertFalse(pointTwo.solved)

    def test_markeSolvedWithObject(self):
        # Setup
        if self.point.solved:
            self.point.markUnsolved()
        self.player.addPointOfInterest(self.point)

        # Testing
        self.player.markSolved(self.point)
        pointTwo = self.player.getPointOfInterest(self.point)
        self.assertTrue(self.point.solved)
        self.assertFalse(pointTwo.solved)

    def test_markUnsolved(self):
        # Setup
        if not self.point.solved:
            self.point.markSolved()
        self.player.addPointOfInterest(self.point)

        # Testing
        self.player.markUnsolved(self.point.name)
        pointTwo = self.player.getPointOfInterest(self.point.name)
        self.assertFalse(self.point.solved)
        self.assertTrue(pointTwo.solved)

    def test_markeUnsolvedWithObject(self):
        # Setup
        if not self.point.solved:
            self.point.markSolved()
        self.player.addPointOfInterest(self.point)

        # Testing
        self.player.markUnsolved(self.point)
        pointTwo = self.player.getPointOfInterest(self.point)
        self.assertFalse(self.point.solved)
        self.assertTrue(pointTwo.solved)

    def test_changeDifficulty(self):
        # Setup
        self.point.changeDifficulty('normal')
        self.player.addPointOfInterest(self.point)

        # Testing
        self.player.changeDifficulty(self.point.name, 'epic')
        pointTwo = self.player.getPointOfInterest(self.point.name)
        self.assertEqual(self.point.difficulty, 'normal')
        self.assertEqual(pointTwo.difficulty, 'epic')

    def test_changeDifficultyWithObject(self):
        # Setup
        self.point.changeDifficulty('normal')
        self.player.addPointOfInterest(self.point)

        # Testing
        self.player.changeDifficulty(self.point, 'epic')
        pointTwo = self.player.getPointOfInterest(self.point)
        self.assertEqual(self.point.difficulty, 'normal')
        self.assertEqual(pointTwo.difficulty, 'epic')

    def test_solvedPoints(self):
        # Setup
        if self.point.solved:
            self.point.markUnsolved()
        pointTwo = PointOfInterest("Test Two", 'epic', True)
        self.player.addPointOfInterest(self.point)
        self.player.addPointOfInterest(pointTwo)

        # Testing
        pointThree = self.player.solvedPoints()
        self.assertEqual(pointThree, pointTwo)
        with self.assertRaises(StopIteration):
            self.player.solvedPoints()

    def test_solvedPointsOrder(self):
        # Setup
        if not self.point.solved:
            self.point.markSolved()
        self.point.changeName("B")
        pointTwo = PointOfInterest("A", 'normal', True)
        self.player.addPointOfInterest(self.point)
        self.player.addPointOfInterest(pointTwo)

        # Testing
        pointThree = self.player.solvedPoints()
        self.assertEqual(pointThree, pointTwo)

    def test_unsolvedPoints(self):
        # Setup
        if not self.point.solved:
            self.point.markSolved()
        pointTwo = PointOfInterest("Test Two", 'epic', False)
        self.player.addPointOfInterest(self.point)
        self.player.addPointOfInterest(pointTwo)

        # Testing
        pointThree = self.player.unsolvedPoints()
        self.assertEqual(pointThree, pointTwo)
        with self.assertRaises(StopIteration):
            self.player.unsolvedPoints()

    def test_unsolvedPointsOrder(self):
        # Setup
        if self.point.solved:
            self.point.markUnsolved()
        self.point.changeName("B")
        pointTwo = PointOfInterest("A", 'normal', False)
        self.player.addPointOfInterest(self.point)
        self.player.addPointOfInterest(pointTwo)

        # Testing
        pointThree = self.player.unsolvedPoints()
        self.assertEqual(pointThree, pointTwo)
