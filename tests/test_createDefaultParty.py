import unittest

from backend.DefaultParty import DefaultParty
from backend.structure.Chair import Chair
from backend.structure.Vending_machine import Vending_machine
from backend.structure.Speaker import Speaker
from backend.structure.Water_fountain import Water_fountain
from backend.structure.Ramp import Ramp
from backend.structure.Scene import Scene
from backend.structure.Stand import Stand
from backend.structure.Tent import Tent
from backend.structure.Toilet import Toilet
from backend.structure.Bodyguard import Bodyguard

"""
[Bodyguard(), Bodyguard(), Bodyguard(), Chaise(), Chaise(), Chaise(), Chaise(), Vending_machine(),
                     Speaker(), Speaker(), Water_fountain(), Ramp(), Scene(), Stand(), Stand(), Stand(), Tent(), Tent(),
                     Toilet(), Toilet()]
"""


class TestCreateDefaultParty(unittest.TestCase):
    def test_CreateDefaultParty(self):
        # Arrange
        expected_party = [
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
            Tent(),
            Tent(),
            Toilet(),
            Toilet(),
            Water_fountain(),
            Stand(),
            Stand(),
            Stand(),
        ]

        # Act
        actual_party = DefaultParty.create()

        # Assert
        self.assertEqual(actual_party.elements, expected_party)
