arr = [2]
k = 1
for i in range(99):
	if(i % 3 == 1):
		arr.append(2 * k)
		k += 1
	else:
		arr.append(1)


num = arr[99]
print(num)
n = 98
deno = 1
for i in range(99):
	temp = num
	num = deno
	deno = temp
	tempNum = num
	num = deno * arr[n - i] + tempNum
	print(num)
	print(deno)

print(num)
