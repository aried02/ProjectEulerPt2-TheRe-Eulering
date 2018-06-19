import SoE
import heapq
h = []
s = SoE.Sieve(7376508).prime_list()
for i in s:
    heapq.heappush(h, i)
x = 1
for i in range(500500):
    l = heapq.heappop(h)
    x = x*l % 500500507
    heapq.heappush(h, l**2)
print(x)
print(heapq.heappop(h))