def fib(n):
    """
    >>> list(fib(5))
    [0, 1, 1, 2, 3]
    >>> list(fib('hi'))
    n must be an integer
    []
    >>> list(fib(-2))
    n must be greater than or equal to 2
    []
    >>>
    """
    try:
        assert isinstance(n, int)
    except AssertionError:
        print("n must be an integer")
        return None

    try:
        assert n >= 2
    except AssertionError:
        print("n must be greater than or equal to 2")
        return None

    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b
