from json import load
from os import stat


def englishWords(wordfile="words_dictionary.json"):
    if not stat(wordfile):
        return False
    else:
        words = {}
        with open(wordfile) as wfile:
            words = load(wfile, encoding='utf-8')
        return words
