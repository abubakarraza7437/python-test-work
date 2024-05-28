# Write a program that maps a list of words into a list of integers representing the lengths of the corresponding
# words.

def words_into_integers(list_of_words):
    list_of_integers = [len(word) for word in list_of_words]
    return list_of_integers


print(words_into_integers(["Hi", "How"]))
