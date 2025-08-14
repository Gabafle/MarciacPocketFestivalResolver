import unittest

from backend.structure.Element import Element
from backend.structure.Stand import Stand


class TestStand(unittest.TestCase):

    def test_InitialisationStandScore(self):
        # Arrange
        expected_value = 100
        stand = Stand()

        # Act
        actual_value = stand.score

        # Assert
        self.assertEqual(actual_value, expected_value)

    def test_CreateStandWidthAndHeight(self):
        # Arrange
        expected_width = 2
        expected_height = 2
        stand = Stand()

        # Act
        actual_width = stand.width
        actual_height = stand.height

        # Assert
        self.assertEqual(actual_width, expected_width)
        self.assertEqual(actual_height, expected_height)

    def test_StandSubClassElement(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Stand, Element))
