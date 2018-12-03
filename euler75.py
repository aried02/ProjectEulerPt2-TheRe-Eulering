# Generate all triples then check numbers
import math2
triples = [0 for i in range(1500001)]
result = 0
for m in range(1, int(((1500000/2)**.5)) + 5):
    for n in range(1, m):
        if math2.gcd(m, n) != 1 or (m % 2 == 1 and n % 2 == 1):
            continue
        a = (m**2 - n**2)
        b = (2*m*n)
        c = m**2 + n**2
        p = a+b+c
        while(p <= 1500000):
            triples[p] += 1
            if triples[p] == 1: result += 1
            elif triples[p] == 2: result -= 1
            p += a+b+c

print(result)