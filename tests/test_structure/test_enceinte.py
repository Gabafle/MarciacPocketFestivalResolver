import unittest

from backend.structure.Element import Element
from backend.structure.Enceinte import Enceinte


class TestEnceinte(unittest.TestCase):
    def testInitialisationEnceinteScore(self):
        # Arrange
        expectedValue = 50
        enceinte = Enceinte()

        # Act
        actualValue = enceinte.score

        # Assert
        self.assertEqual(actualValue, expectedValue)

    def testCreateEnceinteWidthAndHeight(self):
        # Arrange
        expectedWidth = 1
        expectedHeight = 1
        enceinte = Enceinte()

        # Act
        actualWidth = enceinte.width
        actualHeight = enceinte.height

        # Assert
        self.assertEqual(actualWidth, expectedWidth)
        self.assertEqual(actualHeight, expectedHeight)

    def test_enceinte_sub_class_element(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Enceinte, Element))
