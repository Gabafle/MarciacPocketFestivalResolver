import unittest

from backend.structure.Element import Element
from backend.structure.Scene import Scene

class TestScene(unittest.TestCase):
    def test_InitialisationSceneScore(self):
        # Arrange
        expected_value = 100
        scene = Scene()

        # Act
        actual_value = scene.score

        # Assert
        self.assertEqual(actual_value, expected_value)


    def test_CreateSceneWidthAndHeight(self):
        # Arrange
        expected_width = 4
        expected_height = 3
        scene = Scene()

        # Act
        actual_width = scene.width
        actual_height = scene.height

        # Assert
        self.assertEqual(actual_width, expected_width)
        self.assertEqual(actual_height, expected_height)

    def test_SceneSubClassElement(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Scene, Element))
