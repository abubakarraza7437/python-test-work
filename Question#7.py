# Define a function reverse() that computes the reversal of a string. For example, reverse("I am
# testing") should return the string "gnitset ma I".

def reverse_(text):
    return text[:: -1]


print(reverse_("I am testing"))
