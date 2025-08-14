import unittest

from backend.structure.Element import Element
from backend.structure.Stand import Stand


class StandTest(unittest.TestCase):

    def testInitialisationStandScore(self):
        # Arrange
        expectedValue = 100
        stand = Stand()

        # Act
        actualValue = stand.score

        # Assert
        self.assertEqual(actualValue, expectedValue)

    def testCreateStandWidthAndHeight(self):
        # Arrange
        expectedWidth = 2
        expectedHeight = 2
        stand = Stand()

        # Act
        actualWidth = stand.width
        actualHeight = stand.height

        # Assert
        self.assertEqual(actualWidth, expectedWidth)
        self.assertEqual(actualHeight, expectedHeight)

    def test_stand_sub_class_element(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Stand, Element))
