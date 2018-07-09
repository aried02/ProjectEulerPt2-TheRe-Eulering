def fib():
    a = 1
    b = 1
    while True:
        yield a
        tmp = a
        a = a+b
        b = tmp

count = 0
for i in fib():
    if i > 4000000:
        break
    if i%2 == 0:
        count+= i

print(count)