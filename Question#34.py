# Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user,
# builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted
# character frequency table to the screen.

from prettytable import PrettyTable


def char_freq_table(words):
    empty_dict = {}
    for n in words:
        if n in empty_dict:
            empty_dict[n] += 1
        else:
            empty_dict[n] = 1
    return empty_dict


user_input = input("Enter the name of file: ")

with open(user_input) as file:
    content = file.read()

freq_dict = char_freq_table(content)

table = PrettyTable()
table.field_names = ["Word", "frequency"]

for char, freq in freq_dict.items():
    table.add_row([char, freq])

print(table)
