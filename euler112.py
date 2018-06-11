def increasing(n):
    for i in range(len(n)-1):
        if int(n[i]) > int(n[i+1]):
            return False
    return True

def decreasing(n):
    for i in range(len(n)-1):
        if int(n[i]) < int(n[i+1]):
            return False
    return True
bouncy = 0

for i in range(100, 10000000):
    if not increasing(str(i)) and not decreasing(str(i)):
        bouncy = bouncy + 1
    if float(bouncy)/float(i) >= .99:
        print(i)
        break

