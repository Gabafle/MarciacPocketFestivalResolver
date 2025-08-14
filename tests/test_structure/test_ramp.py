import unittest

from backend.structure.Element import Element
from backend.structure.Ramp import Ramp


class TestRamp(unittest.TestCase):

    def test_InitialisationRampScore(self):
        # Arrange
        expected_value = 50
        ramp = Ramp()

        # Act
        actual_value = ramp.score

        # Assert
        self.assertEqual(actual_value, expected_value)

    def test_CreateRampWidthAndHeight(self):
        # Arrange
        expected_width = 1
        expected_height = 1
        ramp = Ramp()

        # Act
        actual_width = ramp.width
        actual_height = ramp.height

        # Assert
        self.assertEqual(actual_width, expected_width)
        self.assertEqual(actual_height, expected_height)

    def test_RampSubClassElement(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Ramp, Element))
