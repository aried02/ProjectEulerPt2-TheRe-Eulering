# Collection of helpful, kinda fast funcs
import fractions
import SoE
import math
from sympy.ntheory import factorint

def phi(n):
    amount = 0
    prod = 1.0
    for p in factorint(n):
        prod = prod*(1.0 - 1.0/p)
    return int(round(n*prod))

def first_n_primes(n):
    # iffy bound, but eh
    top = n*(math.log(n) + math.log(math.log(n)))
    s = SoE.Sieve(int(top)).prime_list()[:n]
    return s

def prime_list_to_n(n):
    s = SoE.Sieve(n).prime_list()
    return s

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

import random, sys

def miller_rabin_pass(a, s, d, n):
    ''' 
    n is an odd number with
        n-1 = (2^s)d, and d odd
        and a is the base: 1 < a < n-1
    
    returns True iff n passes the MillerRabinTest for a 
    '''
    a_to_power = pow(a, d, n)
    i=0
    #Invariant: a_to_power = a^(d*2^i) mod n
    
    # we test whether (a^d) = 1 mod n
    if a_to_power == 1:
        return True
    
    # we test whether a^(d*2^i) = n-1 mod n
    #     for 0<=i<=s-1
    while(i < s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
        i+=1
    
    # we reach here if the test failed until i=s-2    
    return a_to_power == n - 1

def miller_rabin(n):
    '''
    Applies the MillerRabin Test to n (odd)
    
    returns True iff n passes the MillerRabinTest for
    K random bases
    '''
    #Compute s and d such that n-1 = (2^s)d, with d odd
    if n < 2:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0:
        return False
    d = n-1
    s = 0
    while d%2 == 0:
        d >>= 1
        s+=1
    #Applies the test K times
    #The probability of a false positive is less than (1/4)^K
    K = 23
    
    i=1
    while(i<=K):
    # 1 < a < n-1
        a = random.randrange(2,n-1)
        if not miller_rabin_pass(a, s, d, n):
            return False
        i += 1

    return True

        