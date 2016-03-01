import re
import unittest
from shortid import ShortId, shortid


class TestShortId(unittest.TestCase):
    def setUp(self):
        self.shortid = ShortId()

    def test_should_be_unambiquous_on_a_bunch_of_iterations(self):
        ids = []
        for i in range(0, 50000):
            ids.append(self.shortid.generate())

        self.assertEqual(len(set(ids)), len(ids))

    def test_shortid_should_generate_the_right_string_length(self):
        self.assertEqual(len(shortid(7)), 7)

    def test_shortid_should_use_the_right_alphabet(self):
        self.assertTrue(re.match(r'^[a-zA-Z0-9_-]+$', shortid()))

    def test_generate_should_use_the_right_alphabet(self):
        self.assertTrue(re.match(r'^[a-zA-Z0-9_-]+$', self.shortid.generate()))

    def test_generate_should_generate_the_right_string_length(self):
        self.assertTrue(7 <= len(shortid(7)) <= 14)
