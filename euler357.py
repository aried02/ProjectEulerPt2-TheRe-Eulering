from primesieve import primes
import timer
import math
# One day this will run faster than 3 mins
# but that day is not today
@timer.timeit
def euler357(maxi):
    p = primes(maxi)
    s = set(p)
    sol = set()
    acc = [0]
    def recur(termsLeft, start, liststart):
        if termsLeft == 0:
            if start + 1 in s:
                sol.add(start)
                return
        for i in range(liststart, len(p)):
            if p[i]*start >= maxi:
                return
            recur(termsLeft-1, start*p[i], i+1)

    for i in range(8):
       recur(i, 2, 1)
    print("Help me god")
    print(len(sol))
    print(sum(sol))
    tot = 0
    for n in sol:
        # Check each one before adding
        if all( (n%d != 0 or d + n//d in s) for d in range(2, int(math.sqrt(n) + 1))):
            tot = tot + n
    print(tot + 1)


euler357(10**8)