def F():
    a,b = 0,1
    while True:
        yield a
        a, b = b, (a + b) % 1000000000

def isPand(x):
    return ''.join(sorted(x)) == '123456789'
def powLF(n):
    if n == 1:     return (1, 1)
    L, F = powLF(n//2)
    L, F = (L**2 + 5*F**2) >> 1, L*F
    if n & 1:
        return ((L + 5*F)>>1, (L + F) >>1)
    else:
        return (L, F)

def fib(n):
    if n & 1:
        return powLF(n)[1]
    else:
        L, F = powLF(n // 2)
        return L * F

counter = 0
ls = []
for i in F():
    if(isPand(str(i))):
        if(isPand(str(fib(counter))[:9])):
            print(counter)
            break
    counter = counter + 1