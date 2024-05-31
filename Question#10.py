# Define a function overlapping() that takes two lists and returns True if they have at least one member in
# common, False otherwise. You may use your is_member() function, or the in operator, but for the sake
# of the exercise, you should (also) write it using two nested for loops.
import unittest


def overlapping(list1, list2):
    for member1 in list1:
        for member2 in list2:
            if member1 == member2:
                return True
    return False


print(overlapping(["a", "b", "c"], [1, 2, 3, "c"]))


class TestCal(unittest.TestCase):

    def test_overlapping(self):
        result = overlapping(["a", "b", "c"], [1, 2, 3, "c"])
        self.assertEqual(result, True)

    def test_overlapping2(self):
        result = overlapping(["q", "w"], ["r", "t"])
        self.assertEqual(result, False)


test = TestCal
test()
