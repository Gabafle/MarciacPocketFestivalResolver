import unittest

from backend.structure.Vending_machine import Vending_machine
from backend.structure.Element import Element


class TestVendingMachine(unittest.TestCase):
    def test_InitialisationVendingMachineScore(self):
        # Arrange
        expected_value = 50
        vending_machine = Vending_machine()

        # Act
        actual_value = vending_machine.score

        # Assert
        self.assertEqual(actual_value, expected_value)


    def test_CreateDistributeurWidthAndHeight(self):
        # Arrange
        expected_width = 1
        expected_height = 1
        vending_machine = Vending_machine()

        # Act
        actual_width = vending_machine.width
        actual_height = vending_machine.height

        # Assert
        self.assertEqual(actual_width, expected_width)
        self.assertEqual(actual_height, expected_height)

    def test_VendningMachineSubClassElement(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Vending_machine, Element))

