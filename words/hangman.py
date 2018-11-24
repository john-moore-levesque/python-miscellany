import random
import os

# TO DO: add webapp to draw hangman

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def getWords(wordfile="wordfile.txt"):
    try:
        os.stat(wordfile)
    except OSError:
        return False
    words = []
    with open(wordfile, 'r') as wfile:
        words = [word.strip() for word in wfile.readlines()]
    return words


def chooseWord(wordfile="wordfile.txt", wordlist=None):
    if not wordlist:
        wordlist = getWords(wordfile)
    wordchoice = random.choice(wordlist).lower()
    return list(wordchoice)


def setBoard(wordfile="wordfile.txt"):
    wordlist = getWords(wordfile)
    word = chooseWord(wordfile, wordlist)
    board = [None for letter in word]
    penalties = {"head": False, "torso": False, "larm": False, "rarm": False, "lleg": False, "rleg": False}
    while False in penalties.values():
        clear()
        turnsleft = list(penalties.values()).count(False)
        print("%d turns left" %(turnsleft))
        board, penalties = guessLetter(word, board, penalties)
        if board == word:
            clear()
            print(''.join(word))
            return True
    clear()
    print("Answer: %s" %(''.join(word)))
    return False


def penalize(penalties):
    for penalty in penalties.keys():
        if penalties[penalty] is False:
            yield penalty


def guessLetter(word, board, penalties):
    print(board)
    letter = input("Guess a letter: ")
    letter = letter.lower()
    try:
        isinstance(letter, str)
    except AssertionError:
        return False
    if letter in word:
        idx = [i for i, ltr in enumerate(word) if ltr == letter]
        for i in idx:
            board[i] = letter
    else:
        try:
            pnext = penalize(penalties).__next__()
            penalties[pnext] = True
        except StopIteration:
            pass
    return board, penalties


def playGame(wordfile="wordfile.txt"):
    outcome = setBoard(wordfile)
    if outcome:
        print("You win!")
    else:
        print("Better luck next time")


if __name__ == '__main__':
    playGame("wordfile.txt")
