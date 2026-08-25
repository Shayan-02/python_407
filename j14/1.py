def fact(number: int) -> int:
    """
    Get a number and returns factorial of that.

    Args:
        number (int): number that wanna calc factorial of that.

    Returns:
        int: factorial of number
    """
    i = 1
    fact = 1
    while i <= number:
        fact *= i
        i += 1
    return fact


def fact2(number: int) -> int:
    """
    Get a number and returns factorial of that.

    Args:
        number (int): number that wanna calc factorial of that.

    Returns:
        int: factorial of number
    """
    if number == 1:
        return 1
    else:
        return number * fact2(number - 1)

print(fact(5))
print(fact2(5))