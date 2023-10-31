#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import pytest

from prime_jx2552 import is_prime

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


# In[3]:


# Parameterized test for is_prime function
@pytest.mark.parametrize("number, expected_result", [
    (2, True), 
    (7, True), 
    (8, False),  
    (9, False),  
    (1, False), 
    (0, False),    
    (-2, False),   
    (-7, False),   
])

def test_is_prime_param(number, expected_result):
    assert is_prime(number) == expected_result


# In[4]:


# Parameterized test for generate_primes function
@pytest.mark.parametrize("limit, expected_primes", [
    (10, [2, 3, 5, 7]),                 
    (20, [2, 3, 5, 7, 11, 13, 17, 19]), 
    (1, []),                            
    (0, []),                            
    (-10, []),                        
])

def test_generate_primes(limit, expected_primes):
    assert generate_primes(limit) == expected_primes


# In[5]:


# Integration test for prime generation and correctness check
def test_prime_integration():
    # Generate a list of prime numbers up to a limit
    limit = 50 
    generated_primes = generate_primes(limit)

    # Check the correctness of each prime number using the is_prime function
    for num in generated_primes:
        assert is_prime(num) == True

    # check some non-prime numbers to ensure they are correctly identified as non-prime
    for num in range(4, limit + 1):
        if num not in generated_primes:
            assert is_prime(num) == False


# In[6]:


# Run the tests with verbosity (-vv)
if __name__ == "__main__":
    pytest.main(["-vv"])

