import unittest

from backend.structure.Element import Element


class TestElement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.score = 1
        cls.width = 1
        cls.height = 1
        cls.max = 1
        cls.min = 1

    def test_create_element(self):

        # When
        actual_value = Element(self.score, self.width, self.height, self.max, self.min)

        # Then
        self.assertIsInstance(actual_value, Element)
