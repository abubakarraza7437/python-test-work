# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(first_num, sec_num, third_num):
    if first_num > sec_num and third_num:
        return f"{first_num} is the largest number. "
    elif sec_num > first_num and third_num:
        return f"{sec_num} is the largest number. "
    else:
        return f"{third_num} is the largest number. "


print(max_of_three(6, 10, 1))
