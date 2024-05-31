# Write a function filter_long_words() that takes a list of words and an integer n and returns the list of
# words that are longer than n.
import unittest


def filter_long_words(list_of_words, n):
    return [word for word in list_of_words if len(word) >= n]


print(filter_long_words(["data", "data-science", "information", "technology"], 5))


class TestCla(unittest.TestCase):

    def test_filter_long_words(self):
        result = filter_long_words(["data", "data-science", "information", "technology"], 5)
        self.assertEqual(result, ["data-science", "information", "technology"])

    def test_2(self):
        result = filter_long_words(["python", "html", "css", "javascript"], 5)
        self.assertEqual(result, ["python", "javascript"])


if __name__ == "__main__":
    unittest.main()

