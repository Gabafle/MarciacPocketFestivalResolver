from backend.structure.Scene import Scene


def testInitialisationSceneScore():
    # Arrange
    expectedValue = 100
    scene = Scene();

    # Act
    actualValue = scene.score

    # Assert
    assert actualValue == expectedValue


def testCreateSceneWidthAndHeight():
    # Arrange
    expectedWidth = 4
    expectedHeight = 3
    scene = Scene();

    # Act
    actualWidth = scene.width
    actualHeight = scene.height

    # Assert
    assert actualWidth == expectedWidth
    assert actualHeight == expectedHeight
