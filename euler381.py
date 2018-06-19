import SoE
import timer
@timer.timeit
def euler381():
    primes = SoE.Sieve(10**8).prime_list()
    """
    All in the wilson's theorem, so that very minimal calculations are done
    Takes a long time to make the sieve, and no time at all after
    """
    def checkit(p):
        a = (p-1)/2
        if (p+1)%3 == 0:
            b = p - (p+1)/3
        else:
            b = p - (2*p + 1)/3
        
        if (p+1)%4 == 0:
            c = p - (p+1)/4
        else: 
            c = p - (3*p+1)/4
        
        return (a + a*b + a*b*c)%p
    print("Sieve Done"  )
    start = time.time()
    counter = 0
    for i in primes[2:]:
        counter = counter + checkit(i)
    print(counter)
    print("Number of ms after creating sieve")
    print((time.time() - start)*1000)
euler381()