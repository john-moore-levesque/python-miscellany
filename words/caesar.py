import random
import string


def caesar(wordToEncrypt, key=None):
    alpha = string.ascii_lowercase
    wordToEncrypt = wordToEncrypt.lower()
    if not key:
        key = random.randint(1, len(alpha))
    output = []
    for letter in wordToEncrypt:
        if letter.lower() in alpha:
            li = wordToEncrypt.index(letter)
            newletter = alpha[(li + key) % len(alpha)]
            output.append(newletter)
        else:
            output.append(letter)
    return ''.join(output)


if __name__ == '__main__':
    wordToEncrypt = input("Type a word to encrypt: ")
    print(caesar(wordToEncrypt))
