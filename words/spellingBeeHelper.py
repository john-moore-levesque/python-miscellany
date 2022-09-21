# some functions to help with the NYT spelling bee

# Sort the words into lists based on the length of the words, taking a file as input
# this can either be a list of words starting with a specific letter or all the words
def getWordLengths(infile):
    words = {}
    with open(infile, 'r') as f:
        for line in f.readlines():
            l = line.strip('\n')
            ll = len(l)
            if ll in words.keys():
                words[ll].append(l)
            else:
                words[ll] = [l]
    return words

# function to count the number of words based on the starting letter pairs
def wordTally(infile, letterPairs):
    words = { lp : 0 for lp in letterPairs }
    with open(infile, 'r') as f:
        for line in f.readlines():
            for key in words.keys():
                if line[0:2] == key:
                    words[key] += 1
    return words

# function to count the words in a dictionary by length
def wordCountByLength(wDict):
    for key, val in wDict.items():
        print("%d : %d" %(key, len(val)))
