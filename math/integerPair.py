import itertools
import random

def genList(min=-100, max=100, range=25):
    output = []
    while len(output) < range:
        x = random.randint(min, max)
        if -x not in output:
            output.append(x)
    return output

def findIntegerPair(intlist):
    intcomb = list(itertools.combinations(intlist, 2))
    answer = (intcomb[0], sum(intcomb[0]))
    for i in intcomb[1:]:
        s = sum(i)
        if 0 <= s < answer[1] or answer[1] < s <= 0:
            answer = (i, s)
    return answer[0]

if __name__ == "__main__":
	print("For a list of integers, find the integer pair with the sum closest (but not necessarily equal) to 0")
	l = genList()
	print(l)
	print(findIntegerPair(l))
