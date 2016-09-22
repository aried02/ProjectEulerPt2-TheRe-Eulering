import sys

with open("matrix.txt") as f:
    lines = [line.rstrip('\n') for line in f]
    for i in range(len(lines)):
    	lines[i] = lines[i].split(',')
    	for j in range(len(lines[i])):
    		lines[i][j] = int(lines[i][j])

for i in range(len(lines) - 2, -1, -1):
	lines[i][79] += lines[i+1][79]
	print(lines[i][79])
for j in range(len(lines) - 2, -1, -1):
	lines[79][j] += lines[79][j+1]


for j in range(len(lines) - 2, -1, -1):
	for i in range(len(lines) - 2, -1, -1):
		lines[i][j] += min(lines[i+1][j], lines[i][j+1])

print(lines[0][0])