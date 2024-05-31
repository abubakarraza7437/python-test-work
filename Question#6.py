# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list
# of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1,2, 3, 4]) should return 24.
import unittest


def sum(list_of_numbers):
    result = 0
    for n in list_of_numbers:
        result += n
    return result


def multiply(list_of_numbers):
    result = 1
    for n in list_of_numbers:
        result *= n
    return result


print(sum([1, 2, 3, 4]))

print(multiply([1, 2, 3, 4]))


class TestCal(unittest.TestCase):

    def test_sum(self):
        result = sum([1, 2, 3, 4])
        self.assertEqual(result, 10)

    def test_sum2(self):
        result = sum([1, 4])
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = multiply([1, 2, 3, 4])
        self.assertEqual(result, 24)

    def test_multiply2(self):
        result = multiply([1, 4])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()