def isPent(q):
    return (1 + (1 + 4*3*2*q)**.5) % 6 == 0

for i in range(1,10000):
    m = i*(3*i - 1)/2
    for j in range(1,i):
        n = j*(3*j - 1)/2
        if isPent(m + n) and isPent(m - n):
            print m-n
