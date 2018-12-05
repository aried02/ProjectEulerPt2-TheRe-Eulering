from math2 import *
import math
import timer

@timer.timeit
def euler347(N):
    def M(p, q, top):
        # Start with p_exp as log_p(top) - 1, q as 1 and shift to other
        maxim = 0
        maxpexp = math.log(top/q)/math.log(p) + 1
        qexp = math.log(top/p)/math.log(q) + 1
        pexp = int(maxpexp)
        qexp = int(qexp)
        i = pexp
        j = 1
        while(i > 0):
            l = (p**i) * (q**j)
            if l > top:
                i = i - 1
            elif l > maxim:
                maxim = l
                j = j + 1
            else:
                j = j + 1
        return maxim
    ps = prime_list_to_n(N//2 + 1)
    res = []
    for i in range(len(ps)-1):
        if ps[i] > N**.5:
            break
        for j in range(i+1, len(ps)):
            if ps[i] * ps[j] > N:
                break
            l = M(ps[i], ps[j], N)
            if l != 0:
                res.append(l)

    print(sum(res))

#Not as scalable as others, takes 7.5 s noramlly, could be optimized slightly
euler347(10**7)