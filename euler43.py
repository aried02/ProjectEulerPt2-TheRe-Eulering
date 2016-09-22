import itertools as it

ls = it.permutations([0,1,2,3,4,5,6,7,8,9])
primes = [2,3,5,7,11,13,17]
total = 0
def checkGood(i):
    nem = 0;
    counter = 1000000000;
    legit = 0
    if not i[0] == 0:
        for j in range(1,8):
            nem += counter*i[j-1]
            nam = i[j]*100 + i[j+1]*10 + i[j+2]
            if nam%primes[j-1] != 0:
                return 0
            legit+=1
            counter/=10
            if(legit == 7):
                return nem + 100*i[7] + 10 * i[8] + i[9]
    return 0
for i in ls:
    total = total + checkGood(i)
print total
