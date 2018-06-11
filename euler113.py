a = [[-1 for i in range(11)] for y in range(100)]
b = [[-1 for i in range(11)] for y in range(100)]
def numIncreasing(len, max):
    if a[len-1][max] >= 0:
        return a[len-1][max]
    if len == 1:
        a[len-1][max] = max
        return max
    num = 0
    i = 0
    while i <= max:
        num = num + numIncreasing(len-1, i)
        i = i+1
    a[len-1][max] = num
    return num

def numDecreasingp(len, min):
    if b[len-1][min] >= 0:
        return b[len-1][min]
    if len == 1:
        if min == 0:
            b[len-1][min] = 9
            return 9
        b[len-1][min] = 10-min
        return 10-min
    num = 0
    i = 9
    while i >= min:
        num = num + numDecreasingp(len-1, i)
        i = i-1
    b[len-1][min] = num
    return num

def numDecreasing(len):
    num = 0
    for i in range(1, len+1):
        num = num + numDecreasingp(i, 0)
    return num

def decreasing(n):
    for i in range(len(n)-1):
        if int(n[i]) < int(n[i+1]):
            return False
    return True
def increasing(n):
    for i in range(len(n)-1):
        if int(n[i]) > int(n[i+1]):
            return False
    return True
def same(len):
    return 9*len
def nonBounce(len):
    return numIncreasing(len, 10)+numDecreasing(len)- 1 - same(len)

print(nonBounce(100))
    
