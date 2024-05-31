# Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a
# salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet
# ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote
# sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually
# ignored.
import unittest


def palindrome_recognizer(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace(" ", "")
    reverse_phrase = phrase[:: -1]
    if reverse_phrase == phrase:
        return True
    else:
        return False


print(palindrome_recognizer("I roamed under it as a tired nude Maori"))


class TestCal(unittest.TestCase):

    def test_1(self):
        result = palindrome_recognizer("I roamed under it as a tired nude Maori")
        self.assertEqual(result, True)

    def test_2(self):
        result = palindrome_recognizer("Hi there I'm s developer")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()



