# Define a function that computes the length of a given list or string. (It is true that Python has the len()
# function built in, but writing it yourself is nevertheless a good exercise.)

#  For String
import unittest


def length_of_string(string):
    length = 0
    for n in string:
        length += 1
    return length


print(length_of_string("222"))


class TestCal(unittest.TestCase):

    def test_length(self):
        result = length_of_string("12345")
        self.assertEqual(result, 5)

    def test_length2(self):
        result = length_of_string("abcdefgh")
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
