class node:
	def __init__(self, rooti, val):
		self.root = rooti
		self.value = val

def add_div(n):
	total = 1
	for i in range(2, int(n**.5)+1):
		if n%i == 0:
			total+=i
			total+= (n/i)
	return total

def loop(q):
	if not total[add_div(q)] is None:
		return total[add_div(q)]
	if add_div(q) >= 1000:
		return node(None, q)
	else:
		total[q] = node(total[add_div(q)], q)
		q = add_div(q)

i = [n for n in range(1,1000)]
total = [None for n in range(1,1000)]
for n in range(1,999):
	q = n
	while total[q] is None:
		if add_div(q) >= 1000:
			total[q] = node(None, q)
		else:
			total[q] = node(total[add_div(q)], q)
			q = add_div(q)

print 
