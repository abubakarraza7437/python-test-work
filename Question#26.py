# Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers
# and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well
# call the reduce() function directly?

def max_in_list(list_of_numbers):
    return max(list_of_numbers)


print(max_in_list([1, 4, 8, 90]))
