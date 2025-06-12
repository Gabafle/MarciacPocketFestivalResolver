from structure.Stand import Stand



def testInitialisationStandScore():
    # Arrange
    expectedValue = 100
    stand = Stand();

    # Act
    actualValue = stand.score

    # Assert
    assert actualValue == expectedValue


def testCreateStandWidthAndHeight():
    # Arrange
    expectedWidth = 2
    expectedHeight = 2
    stand = Stand();

    # Act
    actualWidth = stand.width
    actualHeight = stand.height

    # Assert
    assert actualWidth == expectedWidth
    assert actualHeight == expectedHeight
