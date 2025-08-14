import unittest

from backend.structure.Distributeur import Distributeur
from backend.structure.Element import Element


class DistributeurTest(unittest.TestCase):
    def testInitialisationDistributeurScore(self):
        # Arrange
        expectedValue = 50
        distributeur = Distributeur()

        # Act
        actualValue = distributeur.score

        # Assert
        self.assertEqual(actualValue, expectedValue)

    def testCreateDistributeurWidthAndHeight(self):
        # Arrange
        expectedWidth = 1
        expectedHeight = 1
        distributeur = Distributeur()

        # Act
        actualWidth = distributeur.width
        actualHeight = distributeur.height

        # Assert
        self.assertEqual(actualWidth, expectedWidth)
        self.assertEqual(actualHeight, expectedHeight)

    def test_distributeur_sub_class_element(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Distributeur, Element))
