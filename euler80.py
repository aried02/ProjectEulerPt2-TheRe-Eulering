from decimal import *
getcontext().prec = 102 #oddly for 100 we are off by 9, 101 off by 1 hm

def digSum(i):
    # Sum first 100 digits of square root
    dec = list(str(Decimal(i).sqrt()))
    dec = filter (lambda x: x != '.', dec)
    dec = map (int, dec)
    res = 0
    for i in range(100):
        res += dec[i]
    return res

perfectsquares = [i**2 for i in range(100)]
res = 0
for j in range(100):
    if j in perfectsquares:
        continue
    res = res + digSum(j)

print(res)