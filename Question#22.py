# In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text
# is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, A
# would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who
# used it to communicate with his generals. ROT13
# ("rotate by 13 places") is a widely used example of a
# Caesar cipher where the shift is 13. In Python, the key for ROT13
# may be represented by means of the
# following dictionary:
# key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t',
# 'h':'u',
# 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b',
# 'p':'c',
# 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j',
# 'x':'k',
# 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R',
# 'F':'S',
# 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z',
# 'N':'A',
# 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H',
# 'V':'I',
# 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
# Your task in this exercise is to implement an encoder/decoder of ROT13.
# Once you're done, you will be
# able to read the following secret message:
# Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
# Note that since English has 26 characters, your ROT13
# program will be able to both encode and decode
# texts written in English.

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = position + shift_amount
        new_letter = alphabets[new_position]
        cipher_text += new_letter
    return f"The encoded text is {cipher_text}."


print(encrypt("hello", 5))


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabets.index(letter)
        new_position = position - shift_amount
        new_letter = alphabets[new_position]
        plain_text += new_letter
    return f"The decoded text is {plain_text}."


print(encrypt("mjqqt", 5))
