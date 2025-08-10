from backend.structure.Enceinte import Enceinte


def testInitialisationEnceinteScore():
    # Arrange
    expectedValue = 50
    enceinte = Enceinte();

    # Act
    actualValue = enceinte.score

    # Assert
    assert actualValue == expectedValue


def testCreateEnceinteWidthAndHeight():
    # Arrange
    expectedWidth = 1
    expectedHeight = 1
    enceinte = Enceinte();

    # Act
    actualWidth = enceinte.width
    actualHeight = enceinte.height

    # Assert
    assert actualWidth == expectedWidth
    assert actualHeight == expectedHeight
