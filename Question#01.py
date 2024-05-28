# Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else
# construct available in Python. (It is true that Python has the max() function built in, but writing it
# yourself is nevertheless a good exercise.)

def max_of_two(first_num, second_num):
    if first_num > second_num:
        return f"{first_num} This is the larger number."
    else:
        return f"{second_num} This is the larger number."


print(max_of_two(2, 5))
