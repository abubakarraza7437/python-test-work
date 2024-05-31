# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained
# in it. Represent the frequency listing as a Python dictionary. Try it with something like
# char_freq("abbabcbdbabdbdbabababcbcbab").
import unittest


def char_freq(sentence):
    empty_dict = {}
    for n in sentence:
        if n in empty_dict:
            empty_dict[n] += 1
        else:
            empty_dict[n] = 1
    return empty_dict


print(char_freq("abbabcbdbabdbdbabababcbcbab"))


class TestCal(unittest.TestCase):

    def test_1(self):
        result = char_freq("abbabcbdbabdbdbabababcbcbab")
        self.assertEqual(result, {'a': 7, 'b': 14, 'c': 3, 'd': 3})

    def test_2(self):
        result = char_freq("mmmm")
        self.assertEqual(result, {'m': 4})


if __name__ == "__main__":
    unittest.main()
