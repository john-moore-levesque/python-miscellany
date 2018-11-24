import math


def rho(x, n):
    """
    >>> rho(2, 10403)
    (101, 103)
    >>> rho(2, 'hi')
    both x and n must be integers
    False
    >>> rho(2.14, 2)
    both x and n must be integers
    False
    >>> rho(-12, 3)
    both x and n must be greater than or equal to 2
    False
    >>>
    """
    try:
        assert isinstance(n, int) and isinstance(x, int)
    except AssertionError:
        print("both x and n must be integers")
        return False

    try:
        assert n >= 2 and x >= 2
    except AssertionError:
        print("both x and n must be greater than or equal to 2")
        return False

    def factoGenerator(x, n):
        # generator for factor
        def g(x, n):
            return (x*x + 1) % n
        y = x
        factor = 1
        while factor == 1:
            x = g(x, n)
            y = g(g(y, n), n)
            factor = math.gcd(abs(x - y), n)
            yield factor

    factor = list(factoGenerator(x, n))[-1]
    if factor == n:
        # If the factor is equal to n, it's prime, so return False
        return False
    else:
        # Otherwise, return the factor and n divided by the factor (as an int)
        return (factor, n//factor)
