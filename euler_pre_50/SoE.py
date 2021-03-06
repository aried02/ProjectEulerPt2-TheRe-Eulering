import numpy as np

class Sieve:
    def __init__(self, max):
        self._max = max
        self._array = [True for i in range(self._max)]
        for i in range(2, self._max):
            if self._array[i]:
                for j in range(i+i, self._max, i):
                    self._array[j] = False
        self._array[0] = False
        self._array[1] = False
    
    def bool_list(self):
        return self._array
    
    def prime_list(self, maxi=None):
        counter = 0
        if maxi is None:
            maxi=self._max
        ls = []
        for i in self._array:
            if counter > maxi:
                return ls
            if i:
                ls.append(counter)
            counter = counter + 1
        return ls
