from backend.structure.Vigile import Vigile


def testInitialisationVigileScore():
    # Arrange
    expectedValue = 100
    vigile = Vigile();

    # Act
    actualValue =vigile.score

    # Assert
    assert actualValue == expectedValue


def testCreateVigileWidthAndHeight():
    # Arrange
    expectedWidth = 1
    expectedHeight = 1
    vigile = Vigile();

    # Act
    actualWidth = vigile.width
    actualHeight = vigile.height

    # Assert
    assert actualWidth == expectedWidth
    assert actualHeight == expectedHeight
