# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False
# otherwise.

def vowel_checker(char):
    vowel_list = ["a", "e", "i", "o", "u"]
    for letter in vowel_list:
        if letter == char:
            return True
        else:
            return False


print(vowel_checker("h"))
