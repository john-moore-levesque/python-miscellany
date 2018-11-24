def bbp(k=10000):
    """
    >>> bbp()
    3.141592653589793
    >>> bbp('hi')
    k must be an integer
    False
    >>> bbp(-12)
    k must be >= 0
    False
    """
    try:
        assert isinstance(k, int)
    except AssertionError:
        print("k must be an integer")
        return False

    try:
        assert k >= 0
    except AssertionError:
        print("k must be >= 0")
        return False

    def bbpPicalc(k):
        yield (1 / (16**k)) * ((4 / (8*k + 1)) - (2 / (8*k + 4)) -
                        (1 / (8*k + 5)) - (1 / (8*k + 6)))

    p = 0
    for i in range(k):
        p += bbpPicalc(i).__next__()
    return p


def leibniz(n=10000):
    """
    >>> leibniz()
    3.1415426535898203
    >>> leibniz('hi')
    n must be an integer
    False
    >>> leibniz(-12)
    n must be >= 0
    False
    """
    try:
        assert isinstance(n, int)
    except AssertionError:
        print("n must be an integer")
        return False

    try:
        assert n >= 0
    except AssertionError:
        print("n must be >= 0")
        return False

    def lbzPicalc(n=10000):
        yield 2 / ((4*n + 1) * (4*n + 3))
    p = 0
    for i in range(n):
        p += lbzPicalc(i).__next__()
    return 4 * p
