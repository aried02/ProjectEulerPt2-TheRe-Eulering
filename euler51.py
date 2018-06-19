from SoE import Sieve
import collections
import re
from timer import timeit
@timeit
def euler51():
    s = Sieve(1000000)

    p = s.prime_list()

    def perms(i):
        i = str(i)
        c = collections.Counter(i).most_common(1)[0]
        if c[1] != 3:
            return []
        c = c[0]
        pr = [re.sub(c, str(j), i) for j in range(10)]
        pr = list(filter(lambda x: x[0] != '0', pr))
        return pr

    for i in p:
        k = perms(i)
        l = list(filter(lambda x: int(x) in p, k))
        if len(l) >= 8:
            print(i)
            print(l)
            break

euler51()