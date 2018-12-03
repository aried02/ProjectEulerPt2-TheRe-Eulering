matrix = []
with open("matrix.txt", "r") as f:
    for line in f.read().split('\n'):
        matrix.append(map(int, line.split(',')))

adjList = {}
#make it into a graph
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        thisNode = i + 100*j
        adjList[thisNode] = []
        for (a, b) in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
            if a < 0 or a >= len(matrix) or b < 0 or b >= len(matrix[0]):
                continue
            adjList[thisNode].append((matrix[a][b], a + b*100))

# Do Djikstras on this
import heapq
def djikstra(X, Q, visited):
    while(len(Q) != 0 and len(visited) < 80*80):
        (d, v) = heapq.heappop(Q)
        if v in visited: continue
        else:
            X[v] = d
            visited.append(v)
            for (w, u) in adjList[v]:
                heapq.heappush(Q, (d+w, u))
    return X

Q = [(0, 0)]
heapq.heapify(Q)
X = djikstra({}, Q, [])
print(X[79 + 79*100] + matrix[0][0])