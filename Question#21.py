# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained
# in it. Represent the frequency listing as a Python dictionary. Try it with something like
# char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(sentence):
    empty_dict = {}
    for n in sentence:
        if n in empty_dict:
            empty_dict[n] += 1
        else:
            empty_dict[n] = 1
    return empty_dict


print(char_freq("abbabcbdbabdbdbabababcbcbab"))
