import unittest

from backend.structure.Element import Element
from backend.structure.Toilette import Toilette

class TestToilette(unittest.TestCase):

    def testInitialisationToiletteScore(self):
        # Arrange
        expectedValue = 100
        toilette = Toilette();

        # Act
        actualValue = toilette.score

        # Assert
        self.assertEqual( actualValue , expectedValue)


    def testCreateToiletteWidthAndHeight(self):
        # Arrange
        expectedWidth = 2
        expectedHeight = 2
        toilette = Toilette();

        # Act
        actualWidth = toilette.width
        actualHeight = toilette.height

        # Assert
        self.assertEqual( actualWidth , expectedWidth)
        self.assertEqual( actualHeight , expectedHeight)

    def test_toilette_sub_class_element(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Toilette, Element))
