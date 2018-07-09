"""
k = #colors
bi = #balls color i
N balls
B = {b1, b2, ..., bk}
Ei(B) set consisting of i-element subsets of B
Qn,c = # ways to choose n elements from ^^ so that number of different colors is c
Qn,c = sum(for E in Ec(B)){ (sum e in E of e) choose n} - sum(i = 1 to c-1) {(k - i choose c-i) * Qn,i

Probability of exactly c colors if you draw n balls is Pn,c = Qn,c / (N choose n)

Expected value = sum(i=1 to k) Pn,i * i


Simplifying, all subsets of B just contain 10, so sum e in E of e = 10*|E|, but |E| in these cases is just c, so sum e in E of e = 10*c, so 

Qn,c = sum(for E in Ec(B))(10*c choose n) - blah
    = |Ec(B)|*(10*c choose n) - blah
    = (k choose c) * (10*c choose n) - blah

Lit
Qn,1 = 0

"""
import timer
@timer.timeit
def euler493():
    k = 7
    N = 70
    nee = 20
    C = [i for i in range(1, 7)]
    Q = [0 for i in range(7)]
    # start at second elem of Q
    def fact(n, acc):
        if n > 1:
            return fact(n-1, n*acc)
        if n == 1:
            return acc
        if n == 0:
            return 1
        return 0
    def combin(n, c):
        if n < c:
            return 0
        if n == c:
            return 1
        num = fact(n, 1)
        den = fact(c, 1) * fact(n-c, 1)
        return num/den

    def compute(n, c):
        return combin(k, c) * combin(10*c, n)

    for i in range(2, 8):
        sub = 0
        for j in range(1, i):
            sub = sub + combin(k-j, i-j)*Q[j-1]
        Q[i-1] = compute(nee, i) - sub
    P = [0 for i in range(7)]
    for i in range(1,7):
        P[i] = float(Q[i]) / combin(N, nee)

    exp = 0
    for i in range(7):
        exp = exp + P[i] * (i+1)

    print(round(exp, 9))

    # Or a better explanations
    # Linearity of expectation, Xi is 1 if color i is in the final 20,
    # 0 if not. P(Xi=1) = 1 - i not chosen, which happens in 60 choose 20 cases
    # out of 70 choose 20

    print(round(7*(1-float(combin(60, 20))/float(combin(70, 20))), 9))

euler493()