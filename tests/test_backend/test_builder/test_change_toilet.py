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


class TestChangeToilet(unittest.TestCase):

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

    def test_changeToiletAddOneToiletOfDefaultParty(self):
        # Given
        expected_party = deepcopy(self.party_custom)
        expected_party.elements.append(Toilet())

        # When
        builder = BuildeurParty(deepcopy(self.party_custom))
        builder.changeToilet(2)
        actual_party = builder.build()

        # Then
        self.assertListEqual(expected_party.elements, actual_party.elements)

    def test_addMaxToiletOfDefaultPartyWithBigValue(self):
        # Given
        expected_value = 2
        builder = BuildeurParty(deepcopy(self.party_custom))

        # When
        builder.changeToilet(7)
        actual_party = builder.build()
        actual_value = actual_party.elements.count(Toilet())

        # Then
        self.assertEqual(expected_value, actual_value)

    def test_addLessToilet(self):
        # Given
        expected_number_toilet = 1
        mutated_party = DefaultParty().create()
        buildeur = BuildeurParty(mutated_party)

        # When
        buildeur.changeToilet(1)
        actual_party = buildeur.build()
        actual_number_toilet = actual_party.elements.count(Toilet())

        # Then
        self.assertEqual(expected_number_toilet, actual_number_toilet)

    def test_addLessToiletOfMin(self):
        # Given
        expected_number_toilet = 1

        party = DefaultParty().create()
        builder = BuildeurParty(party)

        # When
        builder.changeToilet(0)
        actual_party = builder.build()
        actual_number_toilet = actual_party.elements.count(Toilet())

        # Then
        self.assertEqual(expected_number_toilet, actual_number_toilet)
