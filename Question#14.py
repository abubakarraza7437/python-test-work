# Write a program that maps a list of words into a list of integers representing the lengths of the corresponding
# words.
import unittest


def words_into_integers(list_of_words):
    list_of_integers = [len(word) for word in list_of_words]
    return list_of_integers


print(words_into_integers(["Hi", "How"]))


class TestCal(unittest.TestCase):

    def test_words_into_integers(self):
        result = words_into_integers(["hi"])
        self.assertEqual(result, [2])

    def test_words_into_integers2(self):
        result = words_into_integers(["abubakar"])
        self.assertEqual(result, [8])


test = TestCal
test()