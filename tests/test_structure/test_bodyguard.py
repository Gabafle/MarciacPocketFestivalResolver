import unittest

from backend.structure.Element import Element
from backend.structure.Bodyguard import Bodyguard


class TestBodyguard(unittest.TestCase):
    def test_InitialisationBodyguardScore(self):
        # Arrange
        expectedValue = 100
        bodyguard = Bodyguard()

        # Act
        actualValue = bodyguard.score

        # Assert
        self.assertEqual(actualValue, expectedValue)

    def test_CreateBodyguardWidthAndHeight(self):
        # Arrange
        expected_width = 1
        expected_height = 1
        bodyguard = Bodyguard()

        # Act
        actual_width = bodyguard.width
        actual_height = bodyguard.height

        # Assert
        self.assertEqual(actual_width, expected_width)
        self.assertEqual(actual_height, expected_height)

    def test_BodyguardSubClassElement(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Bodyguard, Element))