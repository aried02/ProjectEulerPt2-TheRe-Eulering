import timer
import numpy as np
import collections
import math
@timer.timeit
def euler205():
    def nCr(n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)

    def formula(p, n, s):
        sum = 0
        for k in range((p-n)/s + 1):
            lala = (-1)**k * nCr(n, k) * nCr(p - s*k - 1, n-1)
            sum = sum + lala
        return sum

    pp = {i: formula(i, 9, 4) for i in range(9, 9*4+1)}
    cc = {i: formula(i, 6, 6) for i in range(6, 6*6+1)}
    p = 0.0
    for i in pp:
        s = [cc[j] for j in cc if i > j]
        s = sum(s)
        prob = float(s)/float(6**6) #prob pp beats cc given cc rolled i
        probtwo = float(pp[i])/(4**9) #prob cc rolls i
        total_prob = prob*probtwo
        p = p + total_prob
    print(p)
euler205()