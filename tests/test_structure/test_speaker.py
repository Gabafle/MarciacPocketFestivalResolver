import unittest

from backend.structure.Element import Element
from backend.structure.Speaker import Speaker

class TestSpeaker(unittest.TestCase):
    def test_InitialisationSpeakerScore(self):
        # Arrange
        expected_value = 50
        speaker = Speaker()

        # Act
        actual_value = speaker.score

        # Assert
        self.assertEqual(actual_value,  expected_value)


    def test_CreateSpeakerWidthAndHeight(self):
        # Arrange
        expected_width = 1
        expected_height = 1
        speaker = Speaker()

        # Act
        actual_width = speaker.width
        actual_height = speaker.height

        # Assert
        self.assertEqual(actual_width, expected_width)
        self.assertEqual(actual_height, expected_height)

    def test_SpeakerSubClassElement(self):
        # Given
        # When/Then
        self.assertTrue(issubclass(Speaker, Element))

