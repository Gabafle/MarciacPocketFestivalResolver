import unittest

from backend.structure.Element import Element
from backend.structure.Tente import Tente

class TestTente(unittest.TestCase):
    def testInitialisationTenteScore(self):
        # Arrange
        expectedValue = 100
        tente = Tente()

        # Act
        actualValue = tente.score

        # Assert
        assert actualValue == expectedValue


    def testCreateTenteWidthAndHeight(self):
        # Arrange
        expectedWidth = 3
        expectedHeight = 3
        tente = Tente()

        # Act
        actualWidth = tente.width
        actualHeight = tente.height

        # Assert
        self.assertEqual( actualWidth , expectedWidth)
        self.assertEqual( actualHeight , expectedHeight)

    def test_tente_sub_class_element(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Tente, Element))