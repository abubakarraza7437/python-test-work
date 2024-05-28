# Write a function filter_long_words() that takes a list of words and an integer n and returns the list of
# words that are longer than n.

def filter_long_words(list_of_words, n):
    for word in list_of_words:
        if len(word) < n:
            list_of_words.remove(word)
    return list_of_words


print(filter_long_words(["Bahawalpur", "Lahore", "Karachi", "Paya"], 5))
