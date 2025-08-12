import unittest

from backend.structure.Element import Element
from backend.structure.Fontaine import Fontaine

class TestFontaine(unittest.TestCase):
    def testInitialisationFontaineScore(self):
        # Arrange
        expectedValue = 50
        fontaine = Fontaine()

        # Act
        actualValue = fontaine.score

        # Assert
        self.assertEqual( actualValue , expectedValue)


    def testCreateFontaineWidthAndHeight(self):
        # Arrange
        expectedWidth = 1
        expectedHeight = 1
        fontaine = Fontaine()

        # Act
        actualWidth = fontaine.width
        actualHeight = fontaine.height

        # Assert
        self.assertEqual( actualWidth , expectedWidth)
        self.assertEqual( actualHeight , expectedHeight)

    def test_fontaine_sub_class_element(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Fontaine, Element))