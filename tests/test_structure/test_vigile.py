import unittest

from backend.structure.Element import Element
from backend.structure.Vigile import Vigile


class VigileTest(unittest.TestCase):
    def testInitialisationVigileScore(self):
        # Arrange
        expectedValue = 100
        vigile = Vigile()

        # Act
        actualValue = vigile.score

        # Assert
        self.assertEqual(actualValue, expectedValue)

    def testCreateVigileWidthAndHeight(self):
        # Arrange
        expectedWidth = 1
        expectedHeight = 1
        vigile = Vigile()

        # Act
        actualWidth = vigile.width
        actualHeight = vigile.height

        # Assert
        self.assertEqual(actualWidth, expectedWidth)
        self.assertEqual(actualHeight, expectedHeight)

    def test_vigile_sub_class_element(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Vigile, Element))
