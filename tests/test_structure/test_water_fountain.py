import unittest

from backend.structure.Element import Element
from backend.structure.Water_fountain import Water_fountain


class TestFountain(unittest.TestCase):
    def test_InitialisationFountainScore(self):
        # Arrange
        expected_value = 50
        fountain = Water_fountain()

        # Act
        actual_value = fountain.score

        # Assert
        self.assertEqual(actual_value, expected_value)

    def test_CreateFontaineWidthAndHeight(self):
        # Arrange
        expected_width = 1
        expected_height = 1
        fountain = Water_fountain()

        # Act
        actual_width = fountain.width
        actual_height = fountain.height

        # Assert
        self.assertEqual(actual_width, expected_width)
        self.assertEqual(actual_height, expected_height)

    def testFountainSubClassElement(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Water_fountain, Element))
