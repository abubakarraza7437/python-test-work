# A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The
# quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it
# is a pangram or not.
import unittest


def pangram_checker(sentence):
    list_of_english_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sentence = [*sentence]
    for letter in sentence:
        if letter in list_of_english_alphabets:
            list_of_english_alphabets.remove(letter)
        else:
            continue
    empty_list = []
    if list_of_english_alphabets == empty_list:
        return True
    else:
        return False


print(pangram_checker("The quick brown fox jumps over the lazy dog"))


class TestCal(unittest.TestCase):

    def test_1(self):
        result = pangram_checker("The quick brown fox jumps over the lazy dog")
        self.assertEqual(result, True)

    def test_2(self):
        result = pangram_checker("this is not a pangram sentence")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()