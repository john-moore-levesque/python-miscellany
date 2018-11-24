from englishdictionary import englishWords
import itertools

# TO DO
# Take anagramizer output and turn it into semi-meanigful phrases
# e.g., "astronomer" -> "moon starer"

def disemvoweller(word):
    """
    >>> disemvoweller('hello world')
    'hll wrld'
    >>> disemvoweller('nth')
    'nth'
    >>>
    """
    vowels = "aeiou"
    return ''.join([letter for letter in word if letter not in vowels])


def basicAnagramizer(word, english=None):
    """
    >>> basicAnagramizer('west')
    ['stew', 'tews', 'wets']
    >>>
    """
    if not english:
        english = englishWords()
    sameLength = [key for key in english.keys() if len(key) == len(word)]
    if word in sameLength:
        sameLength.remove(word)
    return [_ for _ in sameLength if sorted(_) == sorted(word)]


def complexAnagramizer(word, english=None):
    """
    >>> word = 'west end'
    >>> anagrams = complexAnagramizer(word)
    >>> len(anagrams)
    134
    >>>
    """
    def sublist(ls1, ls2):
        for element in ls1:
            if element not in ls2:
                return False
        return True

    def filterAnagram(anagram, wordletters):
        '''
        If the anagram is one letter and not "a" or "i", return False
        If the anagram has no vowels, return False
        If the anagram has letters that aren't in the word, return False
        If the anagram has more letters than the word, return False
        Otherwise return True
        '''
        keep = True
        if len(anagram) == 1:
            if anagram != 'a' and anagram != 'i':
                keep = False
        if disemvoweller(anagram) == anagram:
            keep = False
        for aletter in anagram:
            if aletter not in wordletters.keys():
                keep = False
            elif anagram.count(aletter) > wordletters[aletter]:
                keep = False
        return keep

    def runFilter(anagrams, wordletters):
        '''
        filter anagrams
        '''
        for anagram in anagrams:
            if not filterAnagram(anagram, wordletters):
                anagrams.remove(anagram)

    if not english:
        english = englishWords()
    phrase = word.split()
    wordlen = len(word) - word.count(' ')
    anagrams = []
    perm = []
    lettercount = {}
    for letter in ''.join(word.split()):
        if letter not in lettercount.keys():
            lettercount[letter] = word.count(letter)
    for i in range(1, len(phrase) + word.count(' ')):
        perm += list(itertools.permutations(phrase, i+1))
    for p in perm:
        phrase.append(''.join(p))
    for word in phrase:
        for key in english.keys():
            if sublist(word, key) or sublist(key, word):
                if len(key) <= wordlen:
                    anagrams.append(key)
    anagrams = sorted(list(set(anagrams)), key=len)
    alen = len(anagrams)
    aprev = 0
    while alen != aprev:
        aprev = alen
        runFilter(anagrams, lettercount)
        alen = len(anagrams)
    return anagrams
