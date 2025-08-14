import unittest

from backend.random_party import RandomParty
from backend.structure.Chair import Chair
from backend.structure.Vending_machine import Vending_machine
from backend.structure.Speaker import Speaker
from backend.structure.Water_fountain import Water_fountain
from backend.structure.Party import Party
from backend.structure.Ramp import Ramp
from backend.structure.Scene import Scene
from backend.structure.Stand import Stand
from backend.structure.Tent import Tent
from backend.structure.Toilet import Toilet
from backend.structure.Bodyguard import Bodyguard


class TestRandomPartyGenerator(unittest.TestCase):
    def test_ReturnParty(self):
        # when
        actual_value = RandomParty.generate(self)

        # then
        self.assertIsInstance(actual_value, Party)

    def test_MinElements(self):
        # given
        min_bodyguard = 2
        min_chair = 4
        min_vending_machine = 1
        min_speaker = 2
        min_water_fountain = 1
        min_ramp = 1
        min_scene = 1
        min_stand = 1
        min_tent = 1
        min_toilet = 1

        # when
        actual_value = RandomParty.generate(self).elements

        nb_bodyguard = actual_value.count(Bodyguard())
        nb_chair = actual_value.count(Chair())
        nb_vending_machine = actual_value.count(Vending_machine())
        nb_speaker = actual_value.count(Speaker())
        nb_water_fountain = actual_value.count(Water_fountain())
        nb_ramp = actual_value.count(Ramp())
        nb_scene = actual_value.count(Scene())
        nb_stand = actual_value.count(Stand())
        nb_tent = actual_value.count(Tent())
        nb_toilet = actual_value.count(Toilet())

        # then
        self.assertGreaterEqual(nb_bodyguard, min_bodyguard)
        self.assertGreaterEqual(nb_chair, min_chair)
        self.assertGreaterEqual(nb_vending_machine, min_vending_machine)
        self.assertGreaterEqual(nb_speaker, min_speaker)
        self.assertGreaterEqual(nb_water_fountain, min_water_fountain)
        self.assertGreaterEqual(nb_ramp, min_ramp)
        self.assertGreaterEqual(nb_scene, min_scene)
        self.assertGreaterEqual(nb_stand, min_stand)
        self.assertGreaterEqual(nb_tent, min_tent)
        self.assertGreaterEqual(nb_toilet, min_toilet)

    def test_Remaining(self):
        # given
        expected_elements_length = 20

        # when
        actual_elements_length = len(RandomParty.generate(self).elements)

        # then
        self.assertEqual(expected_elements_length, actual_elements_length)
