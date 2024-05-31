# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and
# returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does,
# but for the sake of the exercise you should pretend Python did not have this operator.)
import unittest


def is_member(x):
    check_list = ["a", "b", "c", "d", 1, 2, 4]
    for letter in check_list:
        if x == letter:
            return True
    return False


print(is_member(1))


class TestCal(unittest.TestCase):

    def test_member(self):
        result = is_member("c")
        self.assertEqual(result, True)

    def test_member2(self):
        result = is_member(0)
        self.assertEqual(result, False)


test = TestCal
test()