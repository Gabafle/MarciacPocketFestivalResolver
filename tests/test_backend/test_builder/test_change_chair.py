import unittest
from copy import deepcopy

from backend.DefaultParty import DefaultParty
from backend.buildeur.BuildeurParty import BuildeurParty
from backend.structure.Chair import Chair
from backend.structure.Party import Party


class TestChangeChair(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.party_custom = Party()
        cls.party_custom.elements = []

    def test_changeChaireAddOneChaire(self):
        # Given
        expected_party = deepcopy(self.party_custom)
        expected_party.elements.append(Chair())
        expected_party.elements.append(Chair())
        expected_party.elements.append(Chair())
        expected_party.elements.append(Chair())
        expected_party.elements.append(Chair())

        # When
        builder = BuildeurParty(expected_party)
        builder.changeChair(5)
        actual_party = builder.build()

        # Then
        self.assertListEqual(expected_party.elements, actual_party.elements)

    def test_addMaxChaireOfDefaultPartyWithBigValue(self):
        # Given
        expected_value = 6
        builder = BuildeurParty(deepcopy(self.party_custom))

        # When
        builder.changeChair(7)
        actual_party = builder.build()
        actual_value = actual_party.elements.count(Chair())

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

    def test_addLessChaire(self):
        # Given
        expected_party = DefaultParty().create()
        expected_number_chair = expected_party.elements.count(Chair())
        mutated_party = DefaultParty().create()
        mutated_party.elements.append(Chair())
        buildeur = BuildeurParty(mutated_party)

        # When
        buildeur.changeChair(4)
        actual_party = buildeur.build()
        actual_number_chair = actual_party.elements.count(Chair())

        # Then
        self.assertEqual(expected_number_chair, actual_number_chair)

    def test_addLessChairsOfMin(self):
        # Given
        expected_party = DefaultParty().create()
        expected_number_chair = expected_party.elements.count(Chair())

        party = DefaultParty().create()
        builder = BuildeurParty(party)

        # When
        builder.changeChair(2)
        actual_party = builder.build()
        actual_number_chair = actual_party.elements.count(Chair())

        # Then
        self.assertEqual(expected_number_chair, actual_number_chair)
