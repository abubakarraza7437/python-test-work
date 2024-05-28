# Write a program that maps a list of words into a list of integers representing the lengths of the corresponding
# words. Write it in three different ways: 1) using a forloop, 2) using the higher order function map(), and 3)
# using list comprehensions.

# 1) using a forloop
def length_of_string(list_of_words):
    length = []
    for word in list_of_words:
        length.append(len(word))
    return length


print(length_of_string(["dell", "apple"]))

# 2) using the higher order function map()


def length_of_words_in_list(list_of_string):
    return len(list_of_string)


x = map(length_of_words_in_list, ("dell", "apple"))
print(list(x))


# 3) using list comprehensions.


def length_of_words_in_list_comp(words):
    return [len(word) for word in words]


list_of_words = ["dell", "apple"]
print(length_of_words_in_list_comp(list_of_words))
