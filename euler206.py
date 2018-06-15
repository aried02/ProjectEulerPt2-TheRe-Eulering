# This is really garbage and im sorry
# Split into two, half solved the back of the string, the rest solved the front

def checkGood(x):
    x = str(x)
    if len(x) != 17:
        return False
    p = [x[(i-1)*2] for i in range(1, 10)]
    return p == [str(i) for i in range(1, 10)]

endings = [j for j in range(100, 100000) if str(j**2)[-3] == '8' and str(j**2)[-5] == '7']
endings = ['0' + str(j) for j in endings if len(str(j)) < 5] + [str(j)[-5:] for j in endings if len(str(j)) >= 5]
for i in range(100, 9999):
    ls = [int(str(i) + j) for j in endings]
    ls = map(lambda x: x**2, ls)
    #print(map(lambda x: len(str(x)), ls))
    ls = filter(checkGood, ls)
    if(len(ls) > 0):
        print(ls[0]**.5)
        break
