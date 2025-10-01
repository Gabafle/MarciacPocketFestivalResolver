import unittest
from copy import deepcopy

from backend.buildeur.BuildeurParty import BuildeurParty
from backend.structure.Party import Party
from backend.structure.Speaker import Speaker


class TestChangeSpeaker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.custom_party = Party()
        cls.custom_party.elements = []

    def test_changeSpeakerAddOneSpeakerOfDefaultParty(self):
        # Given
        expected_party = deepcopy(self.custom_party)
        expected_party.elements.append(Speaker())
        expected_party.elements.append(Speaker())
        expected_party.elements.append(Speaker())

        # When
        builder = BuildeurParty(deepcopy(self.custom_party))
        builder.changeSpeaker(3)
        actual_party = builder.build()

        # Then
        self.assertListEqual(expected_party.elements, actual_party.elements)

    def test_addMaxSpeakerOfDefaultPartyWithBigValue(self):
        # Given
        expected_value = 4
        builder = BuildeurParty(deepcopy(self.custom_party))

        # When
        builder.changeSpeaker(7)
        actual_party = builder.build()
        actual_value = actual_party.elements.count(Speaker())

        # Then
        self.assertEqual(expected_value, actual_value)

    def test_inputOtherParty(self):
        # Given
        expected_party = deepcopy(self.custom_party)

        # When
        builder = BuildeurParty(expected_party)
        actual_party = builder.build()

        # Then
        self.assertEqual(expected_party.elements, actual_party.elements)

    def test_addLessSpeaker(self):
        # Given
        expected_number_speaker = 2
        mutated_party = deepcopy(self.custom_party)
        mutated_party.elements.append(Speaker())
        mutated_party.elements.append(Speaker())
        mutated_party.elements.append(Speaker())
        buildeur = BuildeurParty(mutated_party)

        # When
        buildeur.changeSpeaker(2)
        actual_party = buildeur.build()
        actual_number_speaker = actual_party.elements.count(Speaker())

        # Then
        self.assertEqual(expected_number_speaker, actual_number_speaker)

    def test_addLessSpeakerOfMin(self):
        # Given
        expected_number_speaker = 2

        party = deepcopy(self.custom_party)
        builder = BuildeurParty(party)

        # When
        builder.changeSpeaker(1)
        actual_party = builder.build()
        actual_number_speaker = actual_party.elements.count(Speaker())

        # Then
        self.assertEqual(expected_number_speaker, actual_number_speaker)
