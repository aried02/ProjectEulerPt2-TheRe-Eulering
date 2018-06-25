import timer
@timer.timeit
def euler82():
    matrix = []
    with open('p082_matrix.txt') as f:
        for line in f:
            matrix.append(line.split(','))
    for i in matrix:
        i[-1] = i[-1][:-1]

    matrix = map(lambda x: map(int, x), matrix)
    mini = [1000000000]
    smallest_path = [[100000000000]*len(matrix) for i in range(len(matrix))]
    def recur(i, j, acc):
        if j == len(matrix[0])-1:
            acc = acc + matrix[i][j]
            if mini[0] > acc:
                mini[0] = acc
                return
            return
        acc = acc + matrix[i][j]
        if smallest_path[i][j] <= acc or mini[0] <= acc:
            return
        smallest_path[i][j] = acc
        recur(i, j+1, acc)
        if i < len(matrix)-1:
            recur(i+1, j, acc)
        if i > 0:
            recur(i-1, j, acc)
    for i in range(len(matrix)):
        recur(i, 1, matrix[i][0])

    print(mini)

euler82()