# Define a function reverse() that computes the reversal of a string. For example, reverse("I am
# testing") should return the string "gnitset ma I".
import unittest


def reverse(text):
    return text[:: -1]


print(reverse("I am testing"))


class TestCal(unittest.TestCase):

    def test_reverse(self):
        result = reverse("I am testing")
        self.assertEqual(result, "gnitset ma I")


    def test_reverse2(self):
        result = reverse("bill")
        self.assertEqual(result, "llib")



test = TestCal
test()
