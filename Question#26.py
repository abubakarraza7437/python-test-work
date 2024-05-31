# Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers
# and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well
# call the reduce() function directly?
import unittest


def max_in_list(list_of_numbers):
    return max(list_of_numbers)


print(max_in_list([1, 4, 8, 90]))


class TestCal(unittest.TestCase):

    def test_max_in_list_higher_number(self):
        result = max_in_list([1, 4, 8, 90])
        self.assertEqual(result, 90)

    def test_max_in_list(self):
        result = max_in_list([8, 0, 7])
        self.assertEqual(result, 8)


if __name__ == "__main__":
    unittest.main()