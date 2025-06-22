from DefaultParty import createDefaultParty
from structure.Chaise import Chaise
from structure.Distributeur import Distributeur
from structure.Enceinte import Enceinte
from structure.Fontaine import Fontaine
from structure.Party import Party
from structure.Rampe import Rampe
from structure.Scene import Scene
from structure.Stand import Stand
from structure.Tente import Tente
from structure.Toilette import Toilette
from structure.Vigile import Vigile



'''
[Vigile(), Vigile(), Vigile(), Chaise(), Chaise(), Chaise(), Chaise(), Chaise(), Distributeur(),
                     Enceinte(), Enceinte(), Fontaine(), Rampe(), Scene(), Stand(), Stand(), Stand(), Tente(), Tente(),
                     Toilette(), Toilette()]
'''

def test_createDefaultParty():
    # Arrange
    expectedParty = Party()

    expectedParty.scene = Scene()
    expectedParty.rampe = Rampe()
    expectedParty.listVigile = [Vigile(), Vigile(), Vigile()]
    expectedParty.listChaise = [Chaise(), Chaise(), Chaise(), Chaise(), Chaise()]
    expectedParty.listDistributeur = [Distributeur()]
    expectedParty.listEnceinte = [Enceinte(),Enceinte()]
    expectedParty.listTente = [Tente(), Tente()]
    expectedParty.listToilette = [Toilette(), Toilette()]
    expectedParty.listFontaine = [Fontaine()]
    expectedParty.listStand = [Stand(), Stand(), Stand()]

    # Act
    actualParty = createDefaultParty()

    # Assert
    assert actualParty == expectedParty
