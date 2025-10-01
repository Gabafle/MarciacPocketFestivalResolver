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


class TestChangeWaterFontain(unittest.TestCase):

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

    def test_changeWaterFontainAddOneWaterFontainOfDefaultParty(self):
        # Given
        expected_party = deepcopy(self.party_custom)
        expected_party.elements.append(Water_fountain())

        # When
        builder = BuildeurParty(deepcopy(self.party_custom))
        builder.changeWaterFontain(2)
        actual_party = builder.build()

        # Then
        self.assertListEqual(expected_party.elements, actual_party.elements)

    def test_addMaxWaterFontainOfDefaultPartyWithBigValue(self):
        # Given
        expected_value = 2
        builder = BuildeurParty(deepcopy(self.party_custom))

        # When
        builder.changeWaterFontain(7)
        actual_party = builder.build()
        actual_value = actual_party.elements.count(Water_fountain())

        # Then
        self.assertEqual(expected_value, actual_value)

    def test_addLessWaterFontain(self):
        # Given
        expected_number_water_fontain = 1
        mutated_party = deepcopy(self.party_custom)
        mutated_party.elements.append(Water_fountain())
        buildeur = BuildeurParty(mutated_party)

        # When
        buildeur.changeWaterFontain(1)
        actual_party = buildeur.build()
        actual_number_water_fontain = actual_party.elements.count(Water_fountain())

        # Then
        self.assertEqual(expected_number_water_fontain, actual_number_water_fontain)

    def test_addLessWaterFontainOfMin(self):
        # Given
        expected_number_water_fontain = 1

        party = DefaultParty().create()
        builder = BuildeurParty(party)

        # When
        builder.changeWaterFontain(0)
        actual_party = builder.build()
        actual_number_water_fontain = actual_party.elements.count(Water_fountain())

        # Then
        self.assertEqual(expected_number_water_fontain, actual_number_water_fontain)
