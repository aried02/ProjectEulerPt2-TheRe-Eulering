def isPrime(n):
	for i in range(2, int(n**.5) + 1):
		if(n % i == 0):
			return False

	return True;



total = 1
totalPrime = 0

for i in range(1, 100000):
	TL = 4 * i**2 + 1
	TR = 4 * i**2 - 2*i + 1
	BL = 4 * i**2 + 2*i + 1
	if(isPrime(TL)):
		totalPrime += 1
	if(isPrime(TR)):
		totalPrime += 1
	if(isPrime(BL)):
		totalPrime += 1
	total += 4
	if(float(totalPrime)/float(total) <= .1):
		print(2*i + 1)
		break

