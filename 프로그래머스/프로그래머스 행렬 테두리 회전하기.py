def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = (i - 1) * columns + j

    for query in queries:
        minNum = 1e9
        x1, x2, y1, y2 = query[0], query[2], query[1], query[3]

        temp = matrix[x1][y1]
        for i in range(y1 + 1, y2 + 1):
            matrix[x1][i], temp = temp, matrix[x1][i]
            minNum = min(matrix[x1][i], minNum)
        matrix[x1][y1] = matrix[x1 + 1][y1]
        minNum = min(matrix[x1][y1], minNum)

        for i in range(x1 + 1, x2 + 1):
            matrix[i][y2], temp = temp, matrix[i][y2]
            minNum = min(matrix[i][y2], minNum)

        for i in range(y2 - 1, y1 - 1, -1):
            matrix[x2][i], temp = temp, matrix[x2][i]
            minNum = min(matrix[x2][i], minNum)

        for i in range(x2 - 1, x1, -1):
            matrix[i][y1], temp = temp, matrix[i][y1]
            minNum = min(matrix[i][y1], minNum)
        answer.append(minNum)
    return answer