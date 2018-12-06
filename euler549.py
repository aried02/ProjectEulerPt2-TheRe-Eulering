from sympy.ntheory import factorint
from multiprocessing import Pool
mem = {}
for p in [2, 3, 5, 7]:
    resp = [0]
    for j in range(1,27):
        pfact = factorint(p*j)
        resp.append(pfact[p])
    newresp = [sum(resp[:i+1]) for i in range(27)]
    mem[p] = newresp
#now for each pow l map it to which index we need to make that pow
memo = {}
for p in [2, 3, 5, 7]:
    resp = [0 for i in range(27)]
    for l in range(27):
        for i in range(20):
            if mem[p][i] >= l:
                resp[l] = i*p
                break
    memo[p] = resp
        
def s(n):
    pfact = factorint(n)
    maxi = 0
    for p in pfact.keys():
        if pfact[p] < p:
            res = pfact[p]*p
        else:
            res = memo[p][pfact[p]]
        if res > maxi:
            maxi = res
    return maxi

res = 0

