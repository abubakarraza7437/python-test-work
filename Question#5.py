# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's
# language"). That is, double every consonant and place an occurrence of "o" in between. For example,
# translate("this is fun") should return the string "tothohisos isos fofunon".
import unittest

def translate(sentence):
    sentence = sentence.lower()
    list_of_vowel = ["a", "e", "i", "o", "u"]
    translated_sentence = ""
    for letter in sentence:
        if letter.isalpha() and letter not in list_of_vowel:
            translated_sentence += letter + "o" + letter
        else:
            translated_sentence += letter
    return translated_sentence


print(translate("This is fun "))


class TestCal(unittest.TestCase):

    def test_translate(self):
        result = translate("This is fun")
        self.assertEqual(result, "tothohisos isos fofunon")


    def test_translate2(self):
        result = translate("dog")
        self.assertEqual(result, "dodogog")


if __name__ == '__main__':
    unittest.main()