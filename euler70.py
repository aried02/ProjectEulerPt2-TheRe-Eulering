from SoE import Sieve
import itertools
import timer
@timer.timeit
def euler70(maxi):
    def is_perm(a, b):
        return sorted(a) == sorted(b)
    #computes phi for a semi-prime
    def phi(a, b):
        return (a-1)*(b-1)


    s = Sieve(int(10 * maxi**(1./2.)))
    p = s.prime_list()
    p = [i for i in p if i > maxi/p[-1]] # weed em out
    # Get all combos of primes in p with products below 10**7
    li = [(a,b) for (a,b) in itertools.combinations(p, 2) if a*b <= maxi]
    lowest = 2
    l = -1
    for (a,b) in li:
        p = phi(a,b)
        if is_perm(str(p), str(a*b)) and float(a*b)/p < lowest:
            lowest = float(a*b)/p
            l = a*b

    print(l)

euler70(10**7) # takes a little less than a second
euler70(10**8) # takes just a bit longer (about seven seconds)
euler70(10**9) # sheeeeeeesh (like a minute not terrible)


