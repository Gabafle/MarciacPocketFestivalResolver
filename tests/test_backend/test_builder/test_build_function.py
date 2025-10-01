import unittest

from backend.DefaultParty import DefaultParty
from backend.buildeur.BuildeurParty import BuildeurParty
from backend.structure.Chair import Chair
from backend.structure.Party import Party
from backend.structure.Scene import Scene


class TestBuildeur(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.default_party = DefaultParty().create()

    def test_buildReturnDefaultParty(self):
        # Given
        expected_party = self.default_party

        # When
        actual_party = BuildeurParty().build()

        # Then
        self.assertListEqual(expected_party.elements, actual_party.elements)

    def test_build_with_input_party(self):
        # Given
        expected_party = Party()
        expected_party.elements.append(Chair())
        expected_party.elements.append(Scene())

        # When
        actual_party = BuildeurParty(expected_party).build()

        # Then
        self.assertListEqual(expected_party.elements, actual_party.elements)

    def test_build_trow_error_if_sup_20_elements(self):
        # Given
        expected_party = DefaultParty().create()

        # When
        buildeur = BuildeurParty(expected_party)
        buildeur.changeSpeaker(4)
        buildeur.changeBodyguard(4)

        with self.assertRaises(ValueError):
            buildeur.build()
