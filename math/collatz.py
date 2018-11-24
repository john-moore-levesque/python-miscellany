def collatz(n):
    """
    >>> collatz(5)
    [5, 16, 8, 4, 2, 1]
    >>> collatz(-1)
    n must be greater than or equal to 2
    False
    >>> collatz('hi')
    n must be an integer
    False
    >>>
    """
    try:
        assert isinstance(n, int)
    except AssertionError:
        print("n must be an integer")
        return False

    try:
        assert n >= 2
    except AssertionError:
        print("n must be greater than or equal to 2")
        return False

    def collatzGenerator(n):
        while n > 1:
            n = n // 2 if n % 2 == 0 else 3*n + 1
            yield n

    clist = list(collatzGenerator(n))
    clist.insert(0, n)
    return clist
