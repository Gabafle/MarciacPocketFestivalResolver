import unittest

from backend.DefaultParty import DefaultParty
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
from backend.utils.utils_buildeur import UtilsBuildeur


class TestRemoveType(unittest.TestCase):

    def test_remove_chair_type(self):
        # Given
        expected_party = Party()
        expected_party.elements = [
            Bodyguard(),
            Bodyguard(),
            Bodyguard(),
            Scene(),
            Ramp(),
            Vending_machine(),
            Speaker(),
            Speaker(),
            Tent(),
            Tent(),
            Toilet(),
            Toilet(),
            Water_fountain(),
            Stand(),
            Stand(),
            Stand(),
        ]

        ub = UtilsBuildeur()

        # When
        actual_elements_party = ub.remove_by_type(
            DefaultParty.create().elements, [Chair]
        )

        # Then
        self.assertEqual(expected_party.elements, actual_elements_party)
