# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god",
# "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and
# use it to translate your Christmas cards from English into Swedish. That is, write a function translate()
# that takes a list of English words and returns a list of Swedish words.
import unittest
def translate(letter):
    dict_of_words = {
        "merry": "god",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "år"
    }
    list_of_translated_words = []
    for word in letter:
        if word in dict_of_words:
            translated_word = dict_of_words[word]
            list_of_translated_words.append(translated_word)

    return list_of_translated_words


print(translate(["happy", "year", "jul"]))


class TestCal(unittest.TestCase):

    def test_1(self):
        result = translate(["happy"])
        self.assertEqual(result, ["gott"])

    def test_2(self):
        result = translate(["jul"])
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()