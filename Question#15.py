# Write a function find_longest_word() that takes a list of words and returns the length of the longest
# one.
import unittest


def find_longest_word(list_of_words):
    length_of_word = 0
    for word in list_of_words:
        if len(word) > length_of_word:
            length_of_word = len(word)
    return length_of_word


print(find_longest_word(["hi", "How", "How are You?"]))


class TestCal(unittest.TestCase):

    def test_find_longest_word(self):
        result = find_longest_word(["hi", "How", "How are You?"])
        self.assertEqual(result, 12)

    def test_find_longest_word2(self):
        result = find_longest_word(["larger words", "words", "longest words"])
        self.assertEqual(result, 13)


test = TestCal
test()