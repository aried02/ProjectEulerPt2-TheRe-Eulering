from SoE import Sieve

s = Sieve(200000)
p = s.prime_list()
counter = 1
for i in p:
    if counter == 10001:
        print(i)
        break
    counter = counter+1