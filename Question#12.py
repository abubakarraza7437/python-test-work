# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For
# example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******
import unittest


def histogram(list_of_int):
    result = ""
    for num in list_of_int:
        result += "*" * num + "\n"
    return result


print(histogram([4, 9, 7]))


class TestCal(unittest.TestCase):
    def test_histogram(self):
        result = histogram([4])
        self.assertEqual(result, "****\n")

    def test_histogram2(self):
        result = histogram([5])
        self.assertEqual(result, "*****\n")


test = TestCal
test()