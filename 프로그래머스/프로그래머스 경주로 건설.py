from collections import deque


def solution(board):
    length = len(board)

    cost = [[1e9 for _ in range(length)] for _ in range(length)]
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    q = deque()

    for i in range(4):
        q.append([0, 0, i, 0])

    while q:
        x, y, d, c = q.pop()
        for i in range(4):
            moved_x, moved_y = x + move[i][0], y + move[i][1]
            if length > moved_x >= 0 and length > moved_y >= 0 and board[moved_x][moved_y] == 0:
                if d == i:
                    if cost[moved_x][moved_y] >= c + 100:
                        q.append([moved_x, moved_y, i, c + 100])
                        cost[moved_x][moved_y] = c + 100
                    elif cost[moved_x][moved_y] + 600 >= c + 100:
                        q.append([moved_x, moved_y, i, c + 100])
                else:
                    if cost[moved_x][moved_y] >= c + 600:
                        q.append([moved_x, moved_y, i, c + 600])
                        cost[moved_x][moved_y] = c + 600

    return cost[length - 1][length - 1]