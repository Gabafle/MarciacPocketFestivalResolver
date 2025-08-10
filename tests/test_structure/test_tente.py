from backend.structure.Tente import Tente


def testInitialisationTenteScore():
    # Arrange
    expectedValue = 100
    tente = Tente();

    # Act
    actualValue = tente.score

    # Assert
    assert actualValue == expectedValue


def testCreateTenteWidthAndHeight():
    # Arrange
    expectedWidth = 3
    expectedHeight = 3
    tente = Tente();

    # Act
    actualWidth = tente.width
    actualHeight = tente.height

    # Assert
    assert actualWidth == expectedWidth
    assert actualHeight == expectedHeight
