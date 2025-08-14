import unittest

from backend.structure.Element import Element
from backend.structure.Toilet import Toilet


class TestToilet(unittest.TestCase):

    def test_InitialisationToiletteScore(self):
        # Arrange
        expected_value = 100
        toilet = Toilet()

        # Act
        actual_value = toilet.score

        # Assert
        self.assertEqual(actual_value, expected_value)

    def test_CreateToiletteWidthAndHeight(self):
        # Arrange
        expected_width = 2
        expected_height = 2
        toilet = Toilet()

        # Act
        actual_width = toilet.width
        actual_height = toilet.height

        # Assert
        self.assertEqual(actual_width, expected_width)
        self.assertEqual(actual_height, expected_height)

    def test_ToiletSubClassElement(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Toilet, Element))
