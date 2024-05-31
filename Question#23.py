# Define a simple "spelling correction" function correct() that takes a string and sees to it that 1) two or
# more occurrences of the space character is compressed into one, and 2) inserts an extra space after a
# period if the period is directly followed by a letter. E.g. correct("This is very funny and
# cool.Indeed!") should return "This is very funny and cool. Indeed!" Tip: Use regular
# expressions!
import unittest


def correct(sentence):
    sentence = sentence.replace("  ", " ")
    sentence = sentence.replace(".", ". ")
    return sentence


print(correct("This is very funny and cool.Indeed!"))


class TestCal(unittest.TestCase):

    def test_1(self):
        result = correct("This is very funny and cool.Indeed!")
        self.assertEqual(result, "This is very funny and cool. Indeed!")

    def test_2(self):
        result = correct("hi  there.you")
        self.assertEqual(result, "hi there. you")


if __name__ == "__main__":
    unittest.main()


