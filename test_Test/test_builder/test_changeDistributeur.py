from DefaultParty import createDefaultParty
from builder.changeChairs import changeChairs
from builder.changeDistributeur import changeDistributeur
from checkParty import verificationParty
from structure.Chaise import Chaise
from structure.Distributeur import Distributeur


def test_ChangeNumberOfDistributeur():
    # Arrange
    expectedParty = createDefaultParty()
    newListDistributeur = [Distributeur(), Distributeur()]
    expectedParty.listDistributeur = newListDistributeur
    actualParty = createDefaultParty()

    # Act
    actualParty = changeDistributeur(2, actualParty)

    # Assert
    assert actualParty == expectedParty


def test_changeDistributeurNumberMin1():
    # Arrange
    expectedParty = createDefaultParty()
    actualParty = createDefaultParty()

    # Act
    actualParty = changeDistributeur(0, actualParty)

    # Assert
    assert actualParty == expectedParty


def test_changeDistributeurNumberMax3():
    # Arrange
    expectedParty = createDefaultParty()
    expectedParty.listDistributeur = [Distributeur(), Distributeur(), Distributeur()]
    actualParty = createDefaultParty()

    # Act
    actualParty = changeDistributeur(5, actualParty)

    # Assert
    assert actualParty == expectedParty


def test_changeDistributeurNumberCanChangeChairsAndDistributer():
    # Arrange
    expectedParty = createDefaultParty()
    expectedParty.listDistributeur = [Distributeur(), Distributeur()]
    expectedParty.listChaise = [Chaise(), Chaise(), Chaise(), Chaise(), Chaise()]
    actualParty = createDefaultParty()

    # Act
    actualParty = changeDistributeur(2, actualParty)
    actualParty = changeChairs(5, actualParty)

    # assert
    assert actualParty == expectedParty


def test_changeDistributeurIsNOtAParty():
    #Arrange
    expectedParty = createDefaultParty()
    expectedOutput = False
    falseParty = "this is an impostor"

    # Act
    actualOutput = verificationParty(falseParty)
    falseParty = changeDistributeur(2, falseParty)

    # Assert
    assert actualOutput == expectedOutput
    assert falseParty == expectedParty