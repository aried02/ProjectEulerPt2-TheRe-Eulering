def palindrome(x):
    return str(x)[::-1] == str(x)
maxi = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if palindrome(i*j) and i*j > maxi:
            maxi = i*j

print(maxi)