from math2 import *

# We are gonna generate all Rashid numbers first from previous ones
rNums = [[i for i in range(1, 10)]]

def isRashid(i):
    s = sum(map(int, list(i)))
    return int(i) % s == 0
def genRashid(n):
    if n == 13:
        return
    # n is numDigits
    res = []
    for i in rNums[n-1]:
        for j in range(10):
            newi = str(i) + str(j)
            if isRashid(newi):
                res.append(int(newi))
    rNums.append(res)
    genRashid(n+1)
def strong(n):
    s = sum(map(int, list(str(n))))
    return miller_rabin(n/s)

genRashid(1)
primes = []
rNums = map(lambda L: filter(strong, L), rNums)


def genPrimes(n):
    if n == 13:
        return
    res = []
    for i in rNums[n]:
        for j in range(10):
            newi = int(str(i) + str(j))
            if miller_rabin(newi):
                res.append(newi)
    primes.append(res)

    genPrimes(n+1)

genPrimes(0)
print(primes)
print(sum(map(sum, primes)))