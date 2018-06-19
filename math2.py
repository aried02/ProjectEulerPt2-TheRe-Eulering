# Collection of helpful, kinda fast funcs
import fractions
import SoE
import math
from sympy.ntheory import factorint

def phi(n):
    amount = 0
    prod = 1.0
    for p in factorint(n):
        if n % p == 0:
            prod = prod*(1.0 - 1.0/p)
    return int(round(n*prod))

def first_n_primes(n):
    # iffy bound, but eh
    top = n*(math.log(n) + math.log(math.log(n)))
    s = SoE.Sieve(int(top)).prime_list()[:n]
    return s

