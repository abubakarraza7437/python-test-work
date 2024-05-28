# Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and
# prints the line to the screen if it is a palindrome.

def is_palindrome(word):
    reverse_of_word = word[::-1]

    if word == reverse_of_word:
        return f"{word} is palindrome. "
    else:
        return f"{word} is not palindrome. "


user_input = input("Enter the name of file: ")
with open(user_input) as file:
    content = file.read().strip()

print(is_palindrome(content))
