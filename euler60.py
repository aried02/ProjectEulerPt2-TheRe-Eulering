"""
scan across prime

check if can split into two primes, second doesn;t start with 0

if yes check if swapping them yields anything fun

Now we have a list of prime pairs that can be appended to each other

Treat as edges (since they are bidirectional) and try to find a k-clique (shouldn't be that hard, right? rught?????)

I originally tried above and it took way too long but found the answer
Changed it below to take less time based off some of the solutions discussed in
the forum on projecteuler
"""
from SoE import Sieve
import itertools
import timer
# Step one: gen prime list (up to 1,000,000 for now)
@timer.timeit
def euler60():
    s = Sieve(10**4)
    primes = s.prime_list()
    checkpr = s.bool_list()
    size = 5
    tot_res = []
    def is_prime(x):
        for i in range(2, int(x**(1./2.))+1):
            if x % i == 0:
                return False
        return True

    def chain(x):
        if x is None:
            return None
        if len(x) == size:
            return x
        for p in primes:
            if p > x[-1] and check_gucci(x+[p]):
                poss = chain(x+[p])
                if poss is not None:
                    return poss
        return None

    def check_gucci(chain):
        return all(is_prime(int(str(i) + str(j))) for i,j in itertools.permutations(chain, 2))

    for p in primes:
        x = chain([p])
        if x is not None:
            print(x)
            print(sum(x))
            break
euler60()