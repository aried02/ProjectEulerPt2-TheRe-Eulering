import numpy as np

class Sieve:
    def __init__(self, max):
        self._max = max
        self._array = [True for i in range(self._max)]
        for i in range(2, self._max):
            for j in range(i+i, self._max, i):
                self._array[j] = False
        self._array[0] = False
        self._array[1] = False
    
    def bool_list(self):
        return self._array
    
    def prime_list(self):
        counter = 0
        ls = []
        for i in self._array:
            if i:
                ls.append(counter)
            counter = counter + 1
        return ls
