import unittest

from backend.DefaultParty import DefaultParty
from backend.structure.Chaise import Chaise
from backend.structure.Distributeur import Distributeur
from backend.structure.Enceinte import Enceinte
from backend.structure.Fontaine import Fontaine
from backend.structure.Rampe import Rampe
from backend.structure.Scene import Scene
from backend.structure.Stand import Stand
from backend.structure.Tente import Tente
from backend.structure.Toilette import Toilette
from backend.structure.Vigile import Vigile

'''
[Vigile(), Vigile(), Vigile(), Chaise(), Chaise(), Chaise(), Chaise(), Distributeur(),
                     Enceinte(), Enceinte(), Fontaine(), Rampe(), Scene(), Stand(), Stand(), Stand(), Tente(), Tente(),
                     Toilette(), Toilette()]
'''


class TestCreateDefaultParty(unittest.TestCase):
    def testCreateDefaultParty(self):
        # Arrange
        expectedParty = [Vigile(), Vigile(), Vigile(), Chaise(), Chaise(), Chaise(), Chaise(), Scene(), Rampe(),
                         Distributeur(), Enceinte(), Enceinte(), Tente(), Tente(), Toilette(), Toilette(), Fontaine(),
                         Stand(), Stand(), Stand()]

        # Act
        actualParty = DefaultParty.create()

        # Assert
        self.assertEqual(actualParty.elements, expectedParty)
