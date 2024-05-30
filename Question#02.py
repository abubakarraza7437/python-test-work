# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
import unittest


def max_of_three(first_num, sec_num, third_num):
    if first_num > sec_num and third_num:
        return first_num
    elif sec_num > first_num and third_num:
        return sec_num
    else:
        return third_num


print(max_of_three(6, 10, 1))


class TestCal(unittest.TestCase):

    def test_max1(self):
        result = max_of_three(12, 14, 10)
        self.assertEqual(result, 14)

    def test_max2(self):
        result = max_of_three(199, 176, 4)
        self.assertEqual(result, 199)


if __name__ == '__main__':
    unittest.main()