import timer
@timer.timeit
def euler62(N, ceiling):
    l = [i**3 for i in range(ceiling)]
    results = {}
    for i in l:
        s = ''.join(sorted(str(i)))
        results[s] = []
    for i in l:
        s = ''.join(sorted(str(i)))
        results[s].append(i)
        if len(results[s]) >= N:
            print(results[s][0])
            break
        

euler62(5, 10000) #completes in 35 ms or so
euler62(25, 10**6) #for fun, completes in a few seconds