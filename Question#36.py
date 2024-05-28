# A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written
# record of a language, the works of an author, or in a single text. Define a function that given the file name of
# a text will return all its hapaxes. Make sure your program ignores capitalization.

def find_hapaxes(file_name):
    with open(file_name, 'r') as file:
        content = file.read()

    content = content.lower()

    words = content.split()

    word_count = {}
    for word in words:
        word = word.strip('.,!?()[]{}:;\'"')
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    hapaxes = [word for word in word_count if word_count[word] == 1]

    return hapaxes


file_name = 'hapaxes.txt'
hapaxes = find_hapaxes(file_name)
print("Hapaxes:", hapaxes)
