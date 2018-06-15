import timer
@timer.timeit
def euler73():
    s = [[-1]*12001 for j in range(12001)]
    for a in range(len(s)):
        s[a][0] = a
    def gcd(a, b):
        if s[a][b] != -1:
            return s[a][b]
        if b > a:
            return gcd(b, a)
        s[a][b] = gcd(b, a % b)
        return s[a][b]

    def coprimes(b):
        ls = [a for a in range(int(b*(1./3.)+1), int(b*(1./2.)+1)) if gcd(b, a) == 1]
        return len(ls)

    counter = 0
    for i in range(4, 12001):
        counter = counter + coprimes(i) 
    print(counter)
euler73()