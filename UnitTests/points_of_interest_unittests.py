"""Runs unit tests on Points of Interests

This should be run by running unittesting.py in the main foldor
or the imports will fail.
"""
import unittest
from point_of_interest import PointOfInterest


class PointOfIntersetTests(unittest.TestCase):
    """Tests whether the PointOfInterest class is working"""

    def setUp(self):
        self.point = PointOfInterest("Test")

    def test_default(self):
        self.assertEqual(self.point.name, "Test")
        self.assertEqual(self.point.difficulty, 'unknown')
        self.assertFalse(self.point.solved)

    def test_create_custom(self):
        pointTwo = PointOfInterest("TestTwo", 'normal', True)
        self.assertEqual(pointTwo.name, "TestTwo")
        self.assertEqual(pointTwo.difficulty, 'normal')
        self.assertTrue(pointTwo.solved)

    def test_create_invalid(self):
        with self.assertRaises(TypeError):
            pointTwo = PointOfInterest("TestTwo", 'INVALID', True)

    def test_changeName(self):
        self.point.changeName("Test Two")
        self.assertEqual(self.point.name, "Test Two")

    def test_solve(self):
        self.point.markSolved()
        self.assertTrue(self.point.solved)

    def test_unsolve(self):
        self.point.markSolved()
        self.point.markUnsolved()
        self.assertFalse(self.point.solved)

    def test_double_solve(self):
        self.point.markSolved()
        with self.assertRaises(AttributeError):
            self.point.markSolved()

    def test_double_unsolved(self):
        with self.assertRaises(AttributeError):
            self.point.markUnsolved()

    def test_changeDifficulty(self):
        self.point.changeDifficulty('epic')
        self.assertEqual(self.point.difficulty, 'epic')

    def test_changeDifficulty_invalid(self):
        with self.assertRaises(TypeError):
            self.point.changeDifficulty('INVALID')

    def test_compare(self):
        self.point.changeName("A")
        pointTwo = PointOfInterest("B")
        self.assertTrue(PointOfInterest.compareKey(self.point) <
                        PointOfInterest.compareKey(pointTwo))
