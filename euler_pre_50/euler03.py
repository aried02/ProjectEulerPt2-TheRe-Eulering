from sympy.ntheory import factorint

p = factorint(600851475143)

i = max(p.keys())
print(i)