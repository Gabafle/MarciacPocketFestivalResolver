import unittest
from copy import deepcopy

from backend.DefaultParty import DefaultParty
from backend.buildeur.BuildeurParty import BuildeurParty
from backend.structure.Bodyguard import Bodyguard
from backend.structure.Chair import Chair
from backend.structure.Party import Party
from backend.structure.Ramp import Ramp
from backend.structure.Scene import Scene
from backend.structure.Speaker import Speaker
from backend.structure.Stand import Stand
from backend.structure.Tent import Tent
from backend.structure.Toilet import Toilet
from backend.structure.Vending_machine import Vending_machine
from backend.structure.Water_fountain import Water_fountain


class TestChangeVendingMachine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.party_custom = Party()
        cls.party_custom.elements = [
            Bodyguard(),
            Bodyguard(),
            Bodyguard(),
            Chair(),
            Chair(),
            Chair(),
            Chair(),
            Scene(),
            Ramp(),
            Vending_machine(),
            Vending_machine(),
            Speaker(),
            Speaker(),
            Speaker(),
            Tent(),
            Tent(),
            Toilet(),
            Water_fountain(),
            Stand(),
        ]

    def test_inputOtherParty(self):
        # Given
        expected_party = deepcopy(self.party_custom)

        # When
        builder = BuildeurParty(expected_party)
        actual_party = builder.build()

        # Then
        self.assertEqual(expected_party.elements, actual_party.elements)

    def test_changeVendingMachineAddOneVendingMachineOfDefaultParty(self):
        # Given
        expected_party = deepcopy(self.party_custom)
        expected_party.elements.append(Vending_machine())

        # When
        builder = BuildeurParty(deepcopy(self.party_custom))
        builder.changeVendingMachine(3)
        actual_party = builder.build()

        # Then
        self.assertListEqual(expected_party.elements, actual_party.elements)

    def test_addMaxVendingMachineOfDefaultPartyWithBigValue(self):
        # Given
        expected_value = 3
        builder = BuildeurParty(deepcopy(self.party_custom))

        # When
        builder.changeVendingMachine(7)
        actual_party = builder.build()
        actual_value = actual_party.elements.count(Vending_machine())

        # Then
        self.assertEqual(expected_value, actual_value)

    def test_addLessVendingMachine(self):
        # Given
        expected_number_vending_machine = 1
        mutated_party = deepcopy(self.party_custom)
        buildeur = BuildeurParty(mutated_party)

        # When
        buildeur.changeVendingMachine(1)
        actual_party = buildeur.build()
        actual_number_vending_machine = actual_party.elements.count(Vending_machine())

        # Then
        self.assertEqual(expected_number_vending_machine, actual_number_vending_machine)

    def test_addLessVendingMachineOfMin(self):
        # Given
        expected_number_vending_machine = 1

        party = DefaultParty().create()
        builder = BuildeurParty(party)

        # When
        builder.changeVendingMachine(0)
        actual_party = builder.build()
        actual_number_vending_machine = actual_party.elements.count(Vending_machine())

        # Then
        self.assertEqual(expected_number_vending_machine, actual_number_vending_machine)
