
def numDig(a):
	return len(str(a))

numer1 = 3
numer2 = 7
deno1 = 2
deno2 = 5
total = 0

for i in range(1,1000):
	deno2 = numer1 + deno1
	numer2 = deno2 + deno1
	if numDig(numer2) > numDig(deno2):
		total+=1
	numer1 = numer2
	deno1 = deno2

print(total)
