# Define a function that computes the length of a given list or string. (It is true that Python has the len()
# function built in, but writing it yourself is nevertheless a good exercise.)

#  For String

def length_of_string(string):
    length = 0
    for n in string:
        length += 1
    return length


print(length_of_string("222"))


# For List

def length_of_list(lis):
    length = 0
    for n in lis:
        length += 1
    return length


print(length_of_list([1, 5, 8, 9, 0, 10]))
