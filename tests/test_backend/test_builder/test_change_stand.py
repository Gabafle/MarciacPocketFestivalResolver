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


class TestChangeStand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.party_default_custom = Party()
        cls.party_default_custom.elements = [
            Bodyguard(),
            Bodyguard(),
            Chair(),
            Chair(),
            Chair(),
            Scene(),
            Ramp(),
            Vending_machine(),
            Speaker(),
            Speaker(),
            Speaker(),
            Speaker(),
            Tent(),
            Tent(),
            Toilet(),
            Toilet(),
            Water_fountain(),
            Stand(),
        ]

    def test_inputOtherParty(self):
        # Given
        expected_party = deepcopy(self.party_default_custom)
        expected_party.elements.append(Stand())

        # When
        builder = BuildeurParty(expected_party)
        actual_party = builder.build()

        # Then
        self.assertEqual(expected_party.elements, actual_party.elements)

    def test_changeStandAddOneStandOfDefaultParty(self):
        # Given
        expected_party = deepcopy(self.party_default_custom)
        expected_party.elements.append(Stand())

        # When
        builder = BuildeurParty(expected_party)
        builder.changeStand(2)
        actual_party = builder.build()

        # Then
        self.assertListEqual(expected_party.elements, actual_party.elements)

    def test_addMaxStandOfDefaultPartyWithBigValue(self):
        # Given
        expected_value = 3
        default_party = deepcopy(self.party_default_custom)
        builder = BuildeurParty(default_party)

        # When
        builder.changeStand(7)
        actual_party = builder.build()
        actual_value = actual_party.elements.count(Stand())

        # Then
        self.assertEqual(expected_value, actual_value)

    def test_addLessStand(self):
        # Given
        expected_number_stand = 2
        mutated_party = DefaultParty().create()
        buildeur = BuildeurParty(mutated_party)

        # When
        buildeur.changeStand(2)
        actual_party = buildeur.build()
        actual_number_stand = actual_party.elements.count(Stand())

        # Then
        self.assertEqual(expected_number_stand, actual_number_stand)

    def test_addLessStandOfMin(self):
        # Given
        expected_number_stand = 1

        party = DefaultParty().create()
        builder = BuildeurParty(party)

        # When
        builder.changeStand(0)
        actual_party = builder.build()
        actual_number_stand = actual_party.elements.count(Stand())

        # Then
        self.assertEqual(expected_number_stand, actual_number_stand)
