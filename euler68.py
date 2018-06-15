import itertools
import time
start = time.time()
def is_ring_good(ls):
    p = [sum(i) for i in ls]
    return len(set(p)) == 1

nums = [i for i in range(1, 11)]
# end of last set is middle of this one (try other numbers)
def recur(sets, nums_left, sum):
    last = sets[-1][2]
    if len(nums_left)==1:
        num = nums_left[0]
        first = sets[0][1]
        if first+last+num == sum:
            return sets + [(num, last, first)]
        else:
            return None
    
    # Normal execution
    for (i,j) in itertools.permutations(nums_left, 2):
        if i + j + last == sum:
            num_cop = list(nums_left)
            num_cop.remove(i)
            num_cop.remove(j)
            s = recur(sets + [(i, last, j)], num_cop, sum)
            if s is not None:
                return s
    return None
# Borrowed from https://stackoverflow.com/questions/31000591/check-if-a-list-is-a-rotation-of-another-list-that-works-with-duplicates
def cyclic_equiv(u, v):
    n, i, j = len(u), 0, 0
    if n != len(v):
        return False
    while i < n and j < n:
        k = 1
        while k <= n and u[(i + k) % n] == v[(j + k) % n]:
            k += 1
        if k > n:
            return True
        if u[(i + k) % n] > v[(j + k) % n]:
            i += k
        else:
            j += k
    return False

res = []
for (i,j,k) in itertools.permutations(nums, 3):
    cop = nums[:]
    cop.remove(i)
    cop.remove(j)
    cop.remove(k)
    s = recur([(i,j,k)], cop, i+j+k)
    if s is not None:
        res.append(s)

result = []
for j in res:
    if j in res:
        result.append(j)
    res = filter(lambda x: not cyclic_equiv(j, x), res)

ans = result[-1]
print(''.join(map(lambda s: ''.join(map(str, s)), ans)))
print((time.time()-start) * 1000)

