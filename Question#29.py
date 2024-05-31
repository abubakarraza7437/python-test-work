# Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an
# integer n and returns the list of words that are longer than n.
import unittest


def filter_long_words(x, n):
    list_of_larger_words = [word for word in x if len(word) > n]
    return list_of_larger_words


list_of_words = ["computer", "laptop", "bigdata", "datascience"]


print(filter_long_words(list_of_words, 10))


class TestLongWords(unittest.TestCase):

    def test_long_word(self):
        result1 = filter_long_words(["computer", "laptop", "bigdata", "datascience"], 10)
        self.assertEqual(result1, ['datascience'])
        result2 = filter_long_words(["python", "css", "html", "numpy"], 5)
        self.assertEqual(result2, ["python"])


if __name__ == "__main__":
    unittest.main()
