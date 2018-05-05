from math import pow


def formatOutput(val):
    """Adds comma thousands seperator to value, shaves to two decimal points
    Also adds dollar sign
    >>> val = 123456.12345
    >>> newval = formatOutput(val)
    >>> print(newval)
    '$123,456.12'
    """
    return '$' + str(format(val, "3,.2f"))


def compound_principle(principle, rate, compounds, time):
    return principle * pow(1 + rate/compounds, time*compounds)


def compound_contribute(principle, monthly, rate, compounds, time):
    principleInterest = compound_principle(principle, rate, compounds, time)
    monthlyInterest = monthly * \
        ((pow(1 + rate/compounds, compounds*time) - 1)/(rate/compounds)) \
        * (1 + (rate/compounds))
    return principleInterest + monthlyInterest


def getInfo(principle, rate, time, monthly='', compounds=''):
    p, r, t, m, c = map(float, [principle, rate, time, monthly, compounds])
    r = r/100.0
    if not c:
        c = 12
    if not m:
        return formatOutput(compound_principle(p, r, c, t))
    else:
        return formatOutput(compound_contribute(p, m, r, c, t))
