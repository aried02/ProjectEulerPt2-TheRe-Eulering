"""
def gcd(a,b):
	if(b == 0):
		return a
	else:
		return gcd(b, a%b)

max = 0.0
for i in range(10,1000000):
	total = 0.0
	for j in range(1,i):
		if(gcd(i,j) == 1):
			total+=1
	if float(i)/float(total) > max:
		max = float(i)/float(total))

print(max)
"""
def totient(boolpri, n):
	total = 1
	for i in range(2,n):
		if boolpri[i]:
			if(n % i == 0):
				total = total*(1 - i**-1)
	return total*n



arr = [True for i in range(1000000)]
for i in range(2, 1000000):
	if(arr[i] == True):
		for j in range(i*i, 1000000, i):
			arr[j] = False

print(totient(10))