import time

# Generate all four digit triangular, penf etc. numbers
# Check which create a cycle (since its cyclic arbitrarily start with triangle)
# Recursively do it with backtracking
start = time.time()
def t():
    q = lambda n: n*(n+1)/2
    n = 1
    while q(n) <= 9999:
        if n*(n+1)/2 > 999 and n*(n+1)/2 <= 9999: yield n*(n+1)/2
        n = n+1
def s():
    n = 1
    while n**2<= 9999:
        if n**2 > 999 and n**2 <= 9999: yield n**2
        n = n+1
def p():
    q = lambda n: (n*(3*n-1))/2
    n = 1
    while q(n) <= 9999:
        if q(n) > 999 and q(n) <= 9999: yield q(n)
        n = n+1
def hexa():
    q = lambda n: n*(2*n-1)
    n = 1
    while q(n) <= 9999:
        if q(n) > 999 and q(n) <= 9999: yield q(n)
        n = n+1
def hepta():
    q = lambda n: n*(5*n -3)/2
    n = 1
    while q(n) <= 9999:
        if q(n) > 999 and q(n) <= 9999: yield q(n)
        n = n+1
def o():
    q = lambda n: n*(3*n-2)
    n = 1
    while q(n) <= 9999:
        if q(n) > 999 and q(n) <= 9999: yield q(n)
        n = n+1
tri = []
squ = []
pent = []
hexag = []
heptag = []
octa = []
for i in t():
    tri.append(i)
for i in s():
    squ.append(i)
for i in p():
    pent.append(i)
for i in hexa():
    hexag.append(i)
for i in hepta():
    heptag.append(i)
for i in o():
    octa.append(i)

full = [squ, pent, hexag, heptag, octa]
def findit(orig_start, i, rest, succ):
    end = str(i)[-2:]
    if len(rest) == 1:
        lis = rest[0]
        lis = [j for j in lis if str(j) == end+orig_start]
        if len(lis) > 0:
            return succ(lis[0])
        else:
            return None
    for lis in rest:
        rest_tmp = list(rest)
        rest_tmp.remove(lis)
        lis = [j for j in lis if str(j).startswith(end)]
        for j in lis:
            res = findit(orig_start, j, rest_tmp, lambda x: x+j)
            if res is not None:
                return succ(res)
    return None

for i in tri:
    s = findit(str(i)[:2], i, full, lambda x: x+i)
    if s is not None:
        print(s)
        break

print((time.time() - start)*1000)
