from backend.DefaultParty import createDefaultParty
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



'''
[Vigile(), Vigile(), Vigile(), Chaise(), Chaise(), Chaise(), Chaise(), Distributeur(),
                     Enceinte(), Enceinte(), Fontaine(), Rampe(), Scene(), Stand(), Stand(), Stand(), Tente(), Tente(),
                     Toilette(), Toilette()]
'''

def test_createDefaultParty():
    # Arrange
    expectedParty = Party()

    expectedParty.scene = Scene()
    expectedParty.rampe = Rampe()
    expectedParty.listVigile = [Vigile(), Vigile(), Vigile()]
    expectedParty.listChaise = [Chaise(), Chaise(), Chaise(), Chaise()]
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
