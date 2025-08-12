import unittest

from backend.structure.Element import Element
from backend.structure.Scene import Scene

class SceneTest(unittest.TestCase):
    def testInitialisationSceneScore(self):
        # Arrange
        expectedValue = 100
        scene = Scene()

        # Act
        actualValue = scene.score

        # Assert
        self.assertEqual( actualValue , expectedValue)


    def testCreateSceneWidthAndHeight(self):
        # Arrange
        expectedWidth = 4
        expectedHeight = 3
        scene = Scene()

        # Act
        actualWidth = scene.width
        actualHeight = scene.height

        # Assert
        self.assertEqual( actualWidth , expectedWidth)
        self.assertEqual( actualHeight , expectedHeight)

    def test_scene_sub_class_element(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Scene, Element))
