# Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the
# lengths of the word tokens in the text, divided by the number of word tokens).

with open("hapaxes.txt", "r") as file:
    content = file.read()
    content = content.split()
    list_of_length_of_words = []
    for word in content:
        list_of_length_of_words.append(len(word))

average_length_of_words = sum(list_of_length_of_words) / len(list_of_length_of_words)
print(round(average_length_of_words, 0))
