import collections
import functools

class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

def pent(i):
    return i*(3*i - 1)/2

@memoized
def p(n):
    if n < 0: return 0
    elif n == 0: return 1
    return pi(n, 1)

def pi(n, i):
    if n == 0: return 1
    if n < 0: return 0
    if pent(i) > n: return 0
    return (((-1)**(i-1))*p(n - pent(i)) + ((-1)**(i-1))*p(n-pent(-1*i)) + pi(n, i+1)) % 1000000

for n in range(75000):
    #print(n)
    if n% 1000 == 0:
        print(n)
    if p(n) == 0:
        print(n)
        break

