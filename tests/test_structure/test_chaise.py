from backend.structure.Chaise import Chaise


def testCreateChaiseObjectWithScore():
    # Arrange
    expectedValue = 50
    chaise = Chaise()

    # Act
    actualValue = chaise.score

    # Assert
    assert actualValue == expectedValue


def testCreateChaiseWidthAndHeight():
    # Arrange
    expectedWidth = 1
    expectedHeight = 1
    chaise = Chaise()

    # Act
    actualWidth = chaise.width
    actualHeight = chaise.height

    # Assert
    assert actualWidth == expectedWidth
    assert actualHeight == expectedHeight
