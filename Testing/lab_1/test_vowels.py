import unittest
from vowels import count_vowels


class TestCountVowels(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(1, count_vowels("abc"))

    def test_all_vowels(self):
        self.assertEqual(5, count_vowels("aeiou"))

    def test_no_vowels(self):
        self.assertEqual(0, count_vowels("bcd"))


if __name__ == "__main__":
    unittest.main()