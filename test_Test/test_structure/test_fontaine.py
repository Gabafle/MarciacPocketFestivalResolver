from structure.Fontaine import Fontaine


def testInitialisationFontaineScore():
    # Arrange
    expectedValue = 50
    fontaine = Fontaine();

    # Act
    actualValue = fontaine.score

    # Assert
    assert actualValue == expectedValue


def testCreateFontaineWidthAndHeight():
    # Arrange
    expectedWidth = 1
    expectedHeight = 1
    fontaine = Fontaine();

    # Act
    actualWidth = fontaine.width
    actualHeight = fontaine.height

    # Assert
    assert actualWidth == expectedWidth
    assert actualHeight == expectedHeight
