from DefaultParty import createDefaultParty
from builder.changeChairs import changeChairs
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


def test_changeNumbersChairsWith5Chairs():
    # Arrange
    expectedParty = Party()

    expectedParty.scene = Scene()
    expectedParty.rampe = Rampe()
    expectedParty.listVigile = [Vigile(), Vigile(), Vigile()]
    expectedParty.listChaise = [Chaise(), Chaise(), Chaise(), Chaise(), Chaise()]
    expectedParty.listDistributeur = [Distributeur()]
    expectedParty.listEnceinte = [Enceinte(), Enceinte()]
    expectedParty.listTente = [Tente(), Tente()]
    expectedParty.listToilette = [Toilette(), Toilette()]
    expectedParty.listFontaine = [Fontaine()]
    expectedParty.listStand = [Stand(), Stand(), Stand()]

    actualParty = createDefaultParty()

    # Act
    actualParty = changeChairs(5)

    # Assert
    assert actualParty == expectedParty


def test_changeNumbersChairsNotAnNumber():
    # Arrange
    expectedParty = createDefaultParty()

    # Act
    actualParty = createDefaultParty()
    actualParty = changeChairs("fdeyghu")

    # Assert
    assert actualParty == expectedParty

def test_changeNumbersChairsCannotHaveInf4Chairs():
    #Arrange
    expectedParty = createDefaultParty()
    actualParty = createDefaultParty()
    expectedParty.listChaise = [Chaise(), Chaise(), Chaise(),Chaise()]

    #Act
    actualParty = changeChairs(3)

    #Assert
    assert actualParty == expectedParty


def test_changeNumbersChairsCannotHaveSup6Chairs():
    #Arrange
    expectedParty = createDefaultParty()
    actualParty = createDefaultParty()
    expectedParty.listChaise = [Chaise(), Chaise(), Chaise(),Chaise(),Chaise(),Chaise()]

    #Act
    actualParty = changeChairs(7)

    #Assert
    assert actualParty == expectedParty