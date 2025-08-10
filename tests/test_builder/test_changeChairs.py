from backend.DefaultParty import createDefaultParty
from backend.builder.changeChairs import changeChairs
from backend.checkParty import verificationParty
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
    actualParty = changeChairs(5,actualParty)

    # Assert
    assert actualParty == expectedParty


def test_changeNumbersChairsNotAnNumber():
    # Arrange
    expectedParty = createDefaultParty()

    # Act
    actualParty = createDefaultParty()
    actualParty = changeChairs("fdeyghu",actualParty)

    # Assert
    assert actualParty == expectedParty

def test_changeNumbersChairsCannotHaveInf4Chairs():
    #Arrange
    expectedParty = createDefaultParty()
    actualParty = createDefaultParty()
    expectedParty.listChaise = [Chaise(), Chaise(), Chaise(),Chaise()]

    #Act
    actualParty = changeChairs(3,actualParty)

    #Assert
    assert actualParty == expectedParty


def test_changeNumbersChairsCannotHaveSup6Chairs():
    #Arrange
    expectedParty = createDefaultParty()
    actualParty = createDefaultParty()
    expectedParty.listChaise = [Chaise(), Chaise(), Chaise(),Chaise(),Chaise(),Chaise()]

    #Act
    actualParty = changeChairs(7,actualParty)

    #Assert
    assert actualParty == expectedParty

def test_changeNumbersChairsTheSecondParamIsNOtAParty():
    # Arrange
    expectedParty = createDefaultParty()
    expectedOutput = False
    falseParty = "this is an impostor"

    # Act
    actualOutput= verificationParty(falseParty)
    falseParty = changeChairs(2,falseParty)

    # Assert
    assert actualOutput == expectedOutput
    assert falseParty == expectedParty