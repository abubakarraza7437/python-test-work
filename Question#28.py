# Write a function find_longest_word() that takes a list of words and returns the length of the longest
# one. Use only higher order functions.

import unittest


def find_longest_word(list_of_words):
    length_of_word = max(list_of_words)
    return len(length_of_word)


print(find_longest_word(["nestle", "pakistan", "laptop"]))


class TestLongestWord(unittest.TestCase):

    def test_1(self):
        result = find_longest_word(["nestle", "pakistan", "laptop"])
        self.assertEqual(result, 8)

    def test_2(self):
        result = find_longest_word(["Data", "science"])
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()