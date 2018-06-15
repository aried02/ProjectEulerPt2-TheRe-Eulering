import numpy as np
import timer
@timer.timeit
def euler74():
    class Chain:

        def __init__(self, num):
            self.stuff = [num]
            self.circle = []
            self.tail = []
        
        def length(self, n):
            # if part of a cycle, take length of cycle, else tail + cycle
            if n in self.tail:
                return len(self.tail) - self.tail.index(n) + len(self.circle)
            return len(self.circle)

    ls = [None for i in range(10000000)]
    fact = [np.math.factorial(i) for i in range(10)]
    def facty(x):
        x = str(x)
        res = 0
        for i in x:
            res = res + fact[int(i)]
        return res

    for i in range(1000000):
        if ls[i] is not None:
            continue
        k = Chain(i)
        ls[i] = k
        y = facty(i)
        while y not in k.stuff:
            if ls[y] is not None:
                k.circle = ls[y].circle[:] #same cycle however
                k.tail = [i for i in k.stuff if i not in k.circle]
                if y not in k.circle:
                    k.tail = k.tail + (ls[y]).tail[ls[y].tail.index(y):]
                break
            ls[y] = k
            k.stuff.append(y)
            y = facty(y)
        if k.circle == []: 
            k.circle = k.stuff[k.stuff.index(y):]
        if k.tail == []:
            k.tail = [i for i in k.stuff if i not in k.circle]
    # k.stuff for each chain is the full chain with tail start
    # k.circle is just the circle

    counter = 0
    for i in range(1000000):
        if ls[i].length(i) == 60:
            counter = counter + 1
    print(counter)
euler74()