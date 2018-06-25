import timer
@timer.timeit
def euler72(n):
	tot = 0
	phi = [float(i) for i in range(n+1)]
	phi[1] = 0
	for i in range(2, n+1):
		if phi[i] == i:
			for j in range(i, n+1, i):
				phi[j] -= phi[j] / float(i)
	for i in phi:
		tot += int(i)
	print tot

euler72(1000000)