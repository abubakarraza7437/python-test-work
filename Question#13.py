# The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for
# two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose
# we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of
# numbers and returns the largest one.
import unittest


def max_in_list(given_list):
    largest_num = 0
    for num in given_list:
        if num > largest_num:
            largest_num = num
        else:
            largest_num = largest_num
    return largest_num


print(max_in_list([1, 4, 9, 100]))


class TestCal(unittest.TestCase):
    def test_max_in_list(self):
        result = max_in_list([34, 67, 98, 17])
        self.assertEqual(result, 98)

    def test_max_in_list2(self):
        result = max_in_list([4, 9, 10])
        self.assertEqual(result, 10)


test = TestCal
test()