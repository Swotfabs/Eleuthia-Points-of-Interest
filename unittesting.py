"""Runs all of the Unit Tests"""
# Argument Parsing
import argparse

# Unit Tests
import unittest
from UnitTests.points_of_interest_unittests import PointOfIntersetTests
from UnitTests.player_unittests import PlayerTests

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run Unit Tests")
    parser.add_argument('--points', action='store_true', dest='pointTests',
                        help="Runs the Point of Interest Unit Tests")
    parser.add_argument('--players', action='store_true', dest='playerTests',
                        help="Runs the Player Unit Tests")

    args = parser.parse_args()
    suite = unittest.TestSuite()

    if not args.pointTests and not args.playerTests:
        unittest.main()
    if args.pointTests:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(PointOfIntersetTests))
    if args.playerTests:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(PlayerTests))

    unittest.TextTestRunner().run(suite)
