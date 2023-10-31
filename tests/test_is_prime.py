#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import pytest
from prime_jx2552.is_prime import is_prime

# is_prime function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# generate_primes function
def generate_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Test the is_prime function
def test_is_prime():
    # Test with known prime numbers
    assert is_prime(2) == True
    assert is_prime(7) == True

    # Test with known composite numbers
    assert is_prime(8) == False
    assert is_prime(9) == False

# Test the generate_primes function
def test_generate_primes():
    # Test with a small limit (e.g., 10)
    expected_primes_up_to_10 = [2, 3, 5, 7]
    assert generate_primes(10) == expected_primes_up_to_10

    # Test with a larger limit (e.g., 20)
    expected_primes_up_to_20 = [2, 3, 5, 7, 11, 13, 17, 19]
    assert generate_primes(20) == expected_primes_up_to_20

