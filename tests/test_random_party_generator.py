import unittest

from backend.random_party import RandomParty
from backend.structure.Chaise import Chaise
from backend.structure.Distributeur import Distributeur
from backend.structure.Enceinte import Enceinte
from backend.structure.Fontaine import Fontaine
from backend.structure.Party import Party
from backend.structure.Rampe import Rampe
from backend.structure.Scene import Scene
from backend.structure.Stand import Stand
from backend.structure.Tente import Tente
from backend.structure.Toilette import Toilette
from backend.structure.Vigile import Vigile


class TestRandomPartyGenerator(unittest.TestCase):
    def test_return_party(self):
        # when
        actual_value = RandomParty.generate(self)

        # then
        self.assertIsInstance(actual_value, Party)

    def test_min_elements(self):
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
        actual_value = RandomParty.generate(self)

        nb_bodyguard = actual_value.elements.count(Vigile())
        nb_chair = actual_value.elements.count(Chaise())
        nb_vending_machine = actual_value.elements.count(Distributeur())
        nb_speaker = actual_value.elements.count(Enceinte())
        nb_water_fountain = actual_value.elements.count(Fontaine())
        nb_ramp = actual_value.elements.count(Rampe())
        nb_scene = actual_value.elements.count(Scene())
        nb_stand = actual_value.elements.count(Stand())
        nb_tent = actual_value.elements.count(Tente())
        nb_toilet = actual_value.elements.count(Toilette())

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
