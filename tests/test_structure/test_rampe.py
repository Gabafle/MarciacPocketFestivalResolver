from backend.structure.Rampe import Rampe


def testInitialisationRampeScore():
    # Arrange
    expectedValue = 50
    rampe = Rampe();

    # Act
    actualValue = rampe.score

    # Assert
    assert actualValue == expectedValue


def testCreateRampeWidthAndHeight():
    # Arrange
    expectedWidth = 1
    expectedHeight = 1
    rampe = Rampe();

    # Act
    actualWidth = rampe.width
    actualHeight = rampe.height

    # Assert
    assert actualWidth == expectedWidth
    assert actualHeight == expectedHeight
