# Write a program that given a text file will create a new text file in which all the lines from the original file are
# numbered from 1 to n (where n is the number of lines in the file).


with open("text_file.txt", "r") as file:
    contents = file.read()

with open("new_text_file", "w") as new_file:
    n = 0
    while n < 11:
        new_file.write(str(n) + "\n")
        n += 1
