import unittest

from backend.structure.Element import Element
from backend.structure.Rampe import Rampe

class TestRampe(unittest.TestCase):

    def testInitialisationRampeScore(self):
        # Arrange
        expectedValue = 50
        rampe = Rampe()

        # Act
        actualValue = rampe.score

        # Assert
        self.assertEqual( actualValue , expectedValue)


    def testCreateRampeWidthAndHeight(self):
        # Arrange
        expectedWidth = 1
        expectedHeight = 1
        rampe = Rampe()

        # Act
        actualWidth = rampe.width
        actualHeight = rampe.height

        # Assert
        self.assertEqual( actualWidth , expectedWidth)
        self.assertEqual( actualHeight ,expectedHeight)

    def test_rampe_sub_class_element(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Rampe, Element))
