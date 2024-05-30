# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False
# otherwise.
import unittest


def vowel_checker(char):
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in vowel_list:
        if letter == char:
            return True
        else:
            return False


print(vowel_checker("h"))


class TestCal(unittest.TestCase):

    def test_vowel_checker(self):
        result = vowel_checker("d")
        self.assertEqual(result, False)

    def test_vowel_checker2(self):
        result = vowel_checker("a")
        self.assertNotEqual(result, False)


if __name__ == '__main__':
    unittest.main()
