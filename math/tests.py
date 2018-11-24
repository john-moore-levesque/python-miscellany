import doctest
import collatz
import fibonacci
import pollardrho
import pi


def runtests():
    doctest.testmod(collatz)
    doctest.testmod(fibonacci)
    doctest.testmod(pollardrho)
    doctest.testmod(pi)
