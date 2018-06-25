import heapq
from SoE import Sieve
import timer
@timer.timeit
def euler87(n):
    h = []
    s = Sieve(int(n**(1./2.)) + 1)
    p = s.prime_list()
    q = s.prime_list(maxi=int(n**(1./3.)) + 1)
    r = s.prime_list(maxi=int(n**(1./4.)) + 1)
    l = [(i**2 + j**3 + k**4, (i,j,k)) for i in p for j in q for k in r]
    res = []
    for p in l:
        heapq.heappush(h, p)
    while True:
        (a, b) = heapq.heappop(h)
        if a >= 50000000:
            break
        res.append(a)
    print(len(set(res)))

euler87(50000000)