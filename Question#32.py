# Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and
# prints the line to the screen if it is a palindrome.
import unittest


def is_palindrome(word):
    reverse_of_word = word[::-1]

    if word == reverse_of_word:
        return f"{word} is palindrome. "
    else:
        return f"{word} is not palindrome. "


# File name is palindrome words.txt
user_input = input("Enter the name of file: ")
try:
    with open(user_input, "r") as file:
        content = file.read().strip().split()

    for word in content:
        print(is_palindrome(word))
except FileNotFoundError:
    print(f"Error: File '{user_input}' does not exist.")


class TestPalindrome(unittest.TestCase):

    def test_plaindrome(self):
        self.assertEqual(is_palindrome("madam"), "madam is palindrome. ")


test = TestPalindrome
test()
