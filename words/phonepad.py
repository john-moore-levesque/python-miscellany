def makeWord(numbers):
    """
    >>> makeWord('hi')
    False
    >>> makeWord(12)
    False
    >>> makeWord('0000')
    False
    >>> makeWord('222 2 8')
    'cat'
    """
    try:
        assert isinstance(numbers, str)
    except AssertionError:
        return False

    phonepad = {
        """
        0: unused
        1: unused
        2: abc
        3: def
        4: ghi
        5: jkl
        6: mno
        7: pqrs
        8: tuv
        9: wxyz
        """
        '0': None,
        '1': None,
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    word = ''
    letters = numbers.split()
    for letter in letters:
        first = letter[0]
        if letter.count(first) != len(letter):
            return False
        try:
            int(first)
        except ValueError:
            return False
        try:
            assert(int(first) > 1 and int(first) < 10)
        except AssertionError:
            return False
        options = phonepad[first]
        option = options[len(letter) - 1]
        word += option
    return word
