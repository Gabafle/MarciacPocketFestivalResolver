from backend.structure.Toilette import Toilette


def testInitialisationToiletteScore():
    # Arrange
    expectedValue = 100
    toilette = Toilette();

    # Act
    actualValue = toilette.score

    # Assert
    assert actualValue == expectedValue


def testCreateToiletteWidthAndHeight():
    # Arrange
    expectedWidth = 2
    expectedHeight = 2
    toilette = Toilette();

    # Act
    actualWidth = toilette.width
    actualHeight = toilette.height

    # Assert
    assert actualWidth == expectedWidth
    assert actualHeight == expectedHeight
