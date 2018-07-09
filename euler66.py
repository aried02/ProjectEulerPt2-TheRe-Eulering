import math
"""
maxi = 0
maxiD = 0

for D in range(2, 1001):
    if int(D**(1./2.))**2 == D:
        continue
    y = 1
    while True:
        x = int(y*(D**(1./2.)) + 1)
        if x**2 - D*y**2 == 1:
            print("For D {} y {} x is {}".format(D, y, x))
            if x > maxi:
                maxi = x
                maxiD = D
            break
        y = y + 1
print(maxi)
print(maxiD)

TOO SLOW
"""
maxi = 0
maxiD = 0
# we need a convergents method
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
for n in range(2, 1001):
    if int(math.sqrt(n))**2 == n:
        continue
    oga = int(math.sqrt(n))
    a = oga
    onum = 1
    oden = -1*a
    no = oga
    do = 1
    dt = 0
    nt = 1
    # each has unique a, num, den before repeating
    while no**2 - n*do**2 != 1:
        den = n - (oden**2)
        a = int((onum*(oga + -1*oden))/den)
        den = den/gcd(den, onum)
        num = -1*oden - den*a #guaranteed negative
        # res.append((a, den, num))
        # Use a to make hi and ki
        tmpn = a*no +nt
        tmpd = a*do + dt
        nt = no
        dt = do
        no = tmpn
        do = tmpd
        oden = num
        onum = den
    print("For D {} num {} den {}".format(n, no, do))
    if no > maxi:
        maxi = no
        maxiD = n

print(maxi)
print(maxiD)