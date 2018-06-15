from collections import Counter
import time
import timer

@timer.timeit
def doit():
    start = time.time()
    hands = (line.split() for line in open('p054_poker.txt'))
    stuffe = [(hand[:5], hand[5:]) for hand in hands]

    values = {i:r for r,i in enumerate('23456789TJQKA', 2)}
    straights = [(x, x-1, x-2, x-3, x-4) for x in range(14, 5, -1)] + [(14, 5, 4, 3,2)]

    ranks = [(1,1,1,1,1), (2,1,1,1), (2,2,1), (3,1,1), (), (), (3,2), (4,1)]
    def makegood(ls):
        a = []
        b = []
        for i in range(len(ls)):
            a.append(ls[i][0])
            b.append(ls[i][1])
        return [tuple(a), tuple(b)]
    def evalhand(hand):
        #Reverse sort frequency of values:
        stuff = [v[0] for v in hand]
        #Heavily drew inspiration from solution, my b, i will commit seppuku
        ls = sorted(((fre, values[val]) for val,fre in Counter(stuff).items()), reverse=True)
        sc = makegood(ls)
        sc[0] = ranks.index(sc[0])
        if len(set([v[1] for v in hand])) == 1: 
            sc[0] = 5 #flush
        if tuple(sorted(sc[1], reverse=True)) in straights:
            if sc[0] == 5:
                if tuple(sorted(sc[1], reverse=True)) == (14,13,12,11,10): 
                    sc[0] = 9
                else: 
                    sc[0] = 8 #straight flush 
            else:
                sc[0] = 4 #striaght
        return sc
        
    print(len(filter(lambda x: evalhand(x[0]) > evalhand(x[1]), stuffe)))
doit()