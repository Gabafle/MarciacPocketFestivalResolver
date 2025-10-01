import unittest
from copy import deepcopy

from backend.DefaultParty import DefaultParty
from backend.buildeur.BuildeurParty import BuildeurParty
from backend.structure.Bodyguard import Bodyguard
from backend.structure.Party import Party


class TestChangeBodyGuard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.party_custom = Party()
        cls.party_custom.elements = []

    def test_changeBodyGuardAddOneBodyGuard(self):
        # Given
        expected_party = deepcopy(self.party_custom)
        expected_party.elements.append(Bodyguard())
        expected_party.elements.append(Bodyguard())
        expected_party.elements.append(Bodyguard())
        expected_party.elements.append(Bodyguard())

        # When
        builder = BuildeurParty(expected_party)
        builder.changeBodyguard(4)
        actual_party = builder.build()

        # Then
        self.assertListEqual(expected_party.elements, actual_party.elements)

    def test_addMaxBodyGuardWithBigValue(self):
        # Given
        expected_value = 4
        builder = BuildeurParty(deepcopy(self.party_custom))

        # When
        builder.changeBodyguard(7)
        actual_party = builder.build()
        actual_value = actual_party.elements.count(Bodyguard())

        # Then
        self.assertEqual(expected_value, actual_value)

    def test_inputOtherParty(self):
        # Given
        expected_party = deepcopy(self.party_custom)

        # When
        builder = BuildeurParty(expected_party)
        actual_party = builder.build()

        # Then
        self.assertEqual(expected_party.elements, actual_party.elements)

    def test_addLessBodyGuard(self):
        # Given
        expected_number_bodyguard = 2
        mutated_party = DefaultParty().create()
        mutated_party.elements.append(Bodyguard())
        buildeur = BuildeurParty(mutated_party)

        # When
        buildeur.changeBodyguard(1)
        actual_party = buildeur.build()
        actual_number_bodyguard = actual_party.elements.count(Bodyguard())

        # Then
        self.assertEqual(expected_number_bodyguard, actual_number_bodyguard)

    def test_addLessBodyGuardsOfMin(self):
        # Given
        expected_number_bodyguard = 2

        party = DefaultParty().create()
        builder = BuildeurParty(party)

        # When
        builder.changeBodyguard(1)
        actual_party = builder.build()
        actual_number_bodyguard = actual_party.elements.count(Bodyguard())

        # Then
        self.assertEqual(expected_number_bodyguard, actual_number_bodyguard)
