import unittest

from backend.structure.Element import Element
from backend.structure.Tent import Tent


class TestTent(unittest.TestCase):
    def test_InitialisationTentScore(self):
        # Arrange
        expected_value = 100
        tent = Tent()

        # Act
        actual_value = tent.score

        # Assert
        assert actual_value == expected_value

    def test_CreateTentWidthAndHeight(self):
        # Arrange
        expected_width = 3
        expected_height = 3
        tent = Tent()

        # Act
        actual_width = tent.width
        actual_height = tent.height

        # Assert
        self.assertEqual(actual_width, expected_width)
        self.assertEqual(actual_height, expected_height)

    def test_TentSubClassElement(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Tent, Element))
