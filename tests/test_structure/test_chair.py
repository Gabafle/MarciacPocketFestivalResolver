import unittest

from backend.structure.Chair import Chair
from backend.structure.Element import Element


class TestChair(unittest.TestCase):

    def test_CreateChairObjectWithScore(self):
        # Arrange
        expected_value = 50
        chair = Chair()

        # Act
        actual_value = chair.score

        # Assert
        self.assertEqual(actual_value, expected_value)


    def test_CreateChairWidthAndHeight(self):
        # Arrange
        expected_width = 1
        expected_height = 1
        chair = Chair()

        # Act
        actual_width = chair.width
        actual_height = chair.height

        # Assert
        self.assertEqual(actual_width, expected_width)
        self.assertEqual(actual_height, expected_height)


    def test_ChairCubClassElement(self):
        #Given

        #When/Then
        self.assertTrue(issubclass(Chair, Element))


