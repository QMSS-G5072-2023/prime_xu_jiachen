import math

def is_prime(n):
    """
    Check if a number is prime.

    This function takes an integer 'n' as input and returns 'True' if 'n' is a prime number, and 'False' otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: 'True' if the number is prime, 'False' otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True