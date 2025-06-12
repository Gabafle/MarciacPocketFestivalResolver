from structure.Distributeur import Distributeur


def testInitialisationDistributeurScore():
    # Arrange
    expectedValue = 50
    distributeur = Distributeur();

    # Act
    actualValue = distributeur.score

    # Assert
    assert actualValue == expectedValue


def testCreateDistributeurWidthAndHeight():
    # Arrange
    expectedWidth = 1
    expectedHeight = 1
    distributeur = Distributeur();

    # Act
    actualWidth = distributeur.width
    actualHeight = distributeur.height

    # Assert
    assert actualWidth == expectedWidth
    assert actualHeight == expectedHeight
