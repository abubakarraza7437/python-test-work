# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written
# backwards). For example, is_palindrome("radar") should return True
import unittest


def is_palindrome(word):
    reverse_of_word = word[::-1]
    if reverse_of_word == word:
        return True
    else:
        return False


print(is_palindrome("radar"))


class TestCal(unittest.TestCase):

    def test_palindrome(self):
        result = is_palindrome("radar")
        self.assertEqual(result, True)


    def test_palindrome2(self):
        result = is_palindrome("khan")
        self.assertEqual(result, False)


test = TestCal
test()