import unittest

from backend.structure.Chaise import Chaise
from backend.structure.Element import Element


class ChaiseTest(unittest.TestCase):

    def testCreateChaiseObjectWithScore(self):
        # Arrange
        expectedValue = 50
        chaise = Chaise()

        # Act
        actualValue = chaise.score

        # Assert
        self.assertEqual(actualValue, expectedValue)

    def testCreateChaiseWidthAndHeight(self):
        # Arrange
        expectedWidth = 1
        expectedHeight = 1
        chaise = Chaise()

        # Act
        actualWidth = chaise.width
        actualHeight = chaise.height

        # Assert
        self.assertEqual(actualWidth, expectedWidth)
        self.assertEqual(actualHeight, expectedHeight)

    def test_chaise_sub_class_element(self):
        # Given

        # When/Then
        self.assertTrue(issubclass(Chaise, Element))
