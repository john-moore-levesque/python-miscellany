from math import pow


def compound_principle(principle, rate, compounds, time):
    return principle * pow(1 + rate/compounds, time*compounds)


def compound_contribute(principle, monthly, rate, compounds, time):
    principleInterest = compound_principle(principle, rate, compounds, time)
    monthlyInterest = monthly * \
        ((pow(1 + rate/compounds, compounds*time) - 1)/(rate/compounds)) \
        * (1 + (rate/compounds))
    return principleInterest + monthlyInterest


def getInput(prompt):
    """Return the value provided in response to a prompt as a float; returns
    FALSE if it cannot be converted to a float.
    >>> val = getInput('Hi ')
    Hi 5
    >>> print(val)
    5.0
    >>> val = getInput('Hi ')
    Hi there
    >>> print(val)
    False
    """
    value = input("%s " % prompt).replace('%', '')
    try:
        return float(value)
    except ValueError:
        return False


def getInfo():
    """Returns principle, rate, monthly, compounds (i.e., how often interest)
        is compounded), and time
    If rate is >= 1, is divided by 100
    If monthly is left blank, is set to 0 (i.e., no monthly deposits)
    If compounds is left blank, is set to 12 (i.e., compounds monthly)
    """
    prompts = [
        "How much is your initial deposit? ",
        "What is the interest rate, as a percent? ",
        "How much are you adding per month (leave blank for none)? ",
        "How often is the interest compounded (leave blank for 12)? ",
        "How long (in years) will you be letting interest accrue? "
    ]
    principle, rate, monthly, compounds, time = [getInput(prompt)
                                                for prompt in prompts]
    if rate >= 1:
        rate /= 100
    if not monthly:
        monthly = 0
    else:
        monthly = float(monthly)
    if not compounds:
        compounds = 12
    else:
        compounds = float(compounds)
    return principle, rate, monthly, compounds, time


def calculations():
    """Does calculations required to find the final value of an account
    """
    def formatOutput(val):
        """Adds comma thousands seperator to value, shaves to two decimal points
        Also gets currency symbol
        >>> val = 123456.12345
        >>> newval = formatOutput(val)
        Type your currency symbol: $
        >>> print(newval)
        '$123,456.12'
        """
        currSymb = input("Type your currency symbol: ")
        return currSymb + format(val, "3,.2f")

    principle, rate, monthly, compounds, time = getInfo()
    if monthly:
        finalValue = compound_contribute(
            principle, monthly, rate, compounds, time)
    else:
        finalValue = compound_principle(
            principle, rate, compounds, time)
    return finalValue, formatOutput(finalValue)


def main():
    finalValue, finalValueString = calculations()
    return finalValue, finalValueString


if __name__ == '__main__':
    finalValue, finalValueString = main()
    print(finalValueString)
