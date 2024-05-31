# Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else
# construct available in Python. (It is true that Python has the max() function built in, but writing it
# yourself is nevertheless a good exercise.)

import unittest


def max_of_two(first_num, second_num):
    if first_num > second_num:
        return first_num
    else:
        return second_num


print(max_of_two(2, 5))


class TestCal(unittest.TestCase):

    def test_max(self):
        result = max_of_two(20, 30)
        self.assertEqual(result, 30)

    def test_max2(self):
        result = max_of_two(3, 100)
        self.assertEqual(result, 100)


if __name__ == '__main__':
    unittest.main()

