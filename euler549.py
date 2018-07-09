from sympy.ntheory import factorint
from multiprocessing import Pool
def doit(n, i):
    counter = 0
    while i > 0:
        counter = counter + n
        tmp = counter
        while tmp % n == 0:
            i = i - 1
            tmp = tmp // n
    return counter
def stuff(n):
    pfact = factorint(n)
    maxi = 0
    #print(pfact)
    for i in pfact.keys():
        if i*pfact[i] < i**2:
            a = i*pfact[i]
        else:
            a = doit(i, pfact[i])
        if a > maxi:
            maxi = a
    #print(maxi)
    return (maxi, n)
def isPrime(n):
    if n%2 == 0:
        return False
    for i in range(3, int(n**(1./2.)) + 1, 2):
        if n % i == 0:
            return False
    return True
pool = Pool(4)
s = 0
checkpoint = 10**12
for i in pool.imap(stuff, range(2, 10**8 + 1)):
    if s > checkpoint:
        print i[1]
        checkpoint = checkpoint + 10**12
    s = s + i[0]
print s
# Takes a lil long
