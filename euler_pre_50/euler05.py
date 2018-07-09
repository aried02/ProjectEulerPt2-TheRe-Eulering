from sympy.ntheory import factorint
from SoE import Sieve
def euler05(n):
    # Evenly divisible by all numbers from 1-20
    d = {}
    i = Sieve(n+1)
    p = i.prime_list()
    for i in p:
        d[i] = 1

    for j in range(4, n+1):
        f = factorint(j)
        for i in f.keys():
            if f[i] > d[i]:
                d[i] = f[i]
    counter = 1
    for i in d.keys():
        counter = counter * i**d[i]
    print(counter)

euler05(20) #original
euler05(100) #test
euler05(1000) #test2 for fun
