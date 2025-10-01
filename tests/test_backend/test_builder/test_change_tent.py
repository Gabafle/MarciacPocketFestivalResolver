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


class TestChangeTent(unittest.TestCase):

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
            Speaker(),
            Speaker(),
            Speaker(),
            Speaker(),
            Tent(),
            Toilet(),
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

    def test_changeTentAddOneTentOfDefaultParty(self):
        # Given
        expected_party = deepcopy(self.party_custom)
        expected_party.elements.append(Tent())

        # When
        builder = BuildeurParty(deepcopy(self.party_custom))
        builder.changeTent(2)
        actual_party = builder.build()

        # Then
        self.assertListEqual(expected_party.elements, actual_party.elements)

    def test_addMaxTentOfDefaultPartyWithBigValue(self):
        # Given
        expected_value = 2
        builder = BuildeurParty(deepcopy(self.party_custom))

        # When
        builder.changeTent(7)
        actual_party = builder.build()
        actual_value = actual_party.elements.count(Tent())

        # Then
        self.assertEqual(expected_value, actual_value)

    def test_addLessTent(self):
        # Given
        expected_number_tent = 1
        mutated_party = DefaultParty().create()
        buildeur = BuildeurParty(mutated_party)

        # When
        buildeur.changeTent(1)
        actual_party = buildeur.build()
        actual_number_tent = actual_party.elements.count(Tent())

        # Then
        self.assertEqual(expected_number_tent, actual_number_tent)

    def test_addLessTentsOfMin(self):
        # Given
        expected_number_tent = 1

        party = DefaultParty().create()
        builder = BuildeurParty(party)

        # When
        builder.changeTent(0)
        actual_party = builder.build()
        actual_number_tent = actual_party.elements.count(Tent())

        # Then
        self.assertEqual(expected_number_tent, actual_number_tent)
