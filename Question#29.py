# Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an
# integer n and returns the list of words that are longer than n.


def filter_long_words(x, n):
    list_of_larger_words = [word for word in x if len(word) > n]
    return list_of_larger_words


list_of_words = ["pakistan", "japan", "china", "india"]


print(filter_long_words(["pakistan", "japan", "china", "india"], 6))


def filter_long_word(x, n):
    return list(filter(lambda word: len(word) > n, x))


print(filter_long_word(["pakistan", "japan", "china", "india"], 6))
