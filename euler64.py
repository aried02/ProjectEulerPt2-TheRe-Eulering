import math
#n is root to take
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
def doit(n):
    oga = int(math.sqrt(n))
    if oga**2 == n:
        return 0
    a = oga
    res = []
    onum = 1
    oden = -1*a
    # each has unique a, num, den before repeating
    while True:
        den = n - (oden**2)
        a = int((onum*(oga + -1*oden))/den)
        den = den/gcd(den, onum)
        num = -1*oden - den*a #guaranteed negative
        if (a, den, num) in res:
            return len(res)
        res.append((a, den, num))
        oden = num
        onum = den
counter = 0
for i in range(2,10001):
    if doit(i) % 2 == 1:
        counter+=1

print counter