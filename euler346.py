import math
import timer

@timer.timeit
def euler346(big):
    biggestBase = int(((1 + 4*big)**.5)) // 2 + 2

    totRes = []
    for b in range(2, biggestBase):
        # Generate 
        res = b**2 + b + 1
        for i in range(3, int(math.log(big)/math.log(2)) + 2):
            if res >= big:
                break
            totRes.append(res)
            res += b**i

    totRes = list(set(totRes)) 
    print(sum(totRes) + 1)   

euler346(10**12)
#takes 1 sec, 5 for 13, and 22 for 14