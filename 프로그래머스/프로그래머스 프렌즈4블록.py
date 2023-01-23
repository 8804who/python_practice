import heapq


def solution(m, n, board):
    answer = 0
    check = [[0, 1], [1, 0], [1, 1]]
    heap = []
    b = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            b[i][j] = board[i][j]
    board = b

    while True:
        visit = [[False for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                same = False
                if board[i][j] == 0:
                    continue
                for k in range(3):
                    movedX, movedY = i + check[k][0], j + check[k][1]
                    if m > movedX >= 0 and n > movedY >= 0:
                        if board[i][j] != board[movedX][movedY]:
                            break
                        if k == 2:
                            same = True
                if same:
                    if [i, j] not in heap:
                        heapq.heappush(heap, [i, j])
                    for k in range(3):
                        if [i + check[k][0], j + check[k][1]] not in heap:
                            heapq.heappush(heap, [i + check[k][0], j + check[k][1]])

        if not heap:
            break
        while heap:
            x, y = heapq.heappop(heap)
            while x > 0:
                board[x][y] = board[x - 1][y]
                x -= 1
            board[x][y] = 0

    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    return answer