#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def is_prime(n):
    """
    Check if a number is prime.

    This function takes an integer 'n' as input and returns True if 'n' is a prime number,
    or False if it is not.

    Parameters:
        n (int): The number to check for primality.

    Returns:
        bool: True if 'n' is prime, False otherwise.

    Example:
        >>> is_prime(17)
        True
        >>> is_prime(20)
        False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

