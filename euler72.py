def totient(n):
	total = 1
	for i in range(2,n):
		if arr[i]:
			if(n % i == 0):
				total = total*(1 - i**-1)
	return total*n


lent = 1000000
arr = [True for i in range(lent)]
for i in range(2, lent):
	if(arr[i] == True):
		for j in range(i*i, lent, i):
			arr[j] = False

tot = 0
for i in range(2, 1000000):
	tot = tot + totient(i)

print tot