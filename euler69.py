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

arr = [True for i in range(50)]
for i in range(2, 50):
	if(arr[i] == True):
		for j in range(i*i, 50, i):
			arr[j] = False
total = 1
for i in range(2,50):
	if arr[i]:
		if(total * i > 50):
			print(total)
			break
		else:
			total = total*i
