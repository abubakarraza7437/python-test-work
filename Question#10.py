# Define a function overlapping() that takes two lists and returns True if they have at least one member in
# common, False otherwise. You may use your is_member() function, or the in operator, but for the sake
# of the exercise, you should (also) write it using two nested for loops.

def overlapping(list1, list2):
    for member1 in list1:
        for member2 in list2:
            if member1 == member2:
                return True
    return False


print(overlapping(["a", "b", "c"], [1, 2, 3, "c"]))
