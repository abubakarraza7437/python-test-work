# Write a function find_longest_word() that takes a list of words and returns the length of the longest
# one. Use only higher order functions.

def find_longest_word(list_of_words):
    length_of_word = max(list_of_words)
    return len(length_of_word)


print(find_longest_word(["nestle", "pakistan", "laptop"]))
