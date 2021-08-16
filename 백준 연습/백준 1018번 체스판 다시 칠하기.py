import sys

n, m = map(int, sys.stdin.readline().split())
board = [[]]
for i in range(n):
    board.append(str(sys.stdin.readline().split())[1:-2])
small = n*m
for i in range(1, n - 6):
    for j in range(1, m - 6):
        count = 0
        for row in range(i, i + 8):
            if (row - i) % 2 != 0:  # 짝수 행
                for col in range(j, j + 8):
                    if (col - j) % 2 != 0 and board[row][col] != board[i][j]:  # 짝수 열
                        count += 1
                    elif (col - j) % 2 == 0 and board[row][col] == board[i][j]:  # 홀수 열
                        count += 1
            else:  # 홀수 행
                for col in range(j, j + 8):
                    if (col - j) % 2 != 0 and board[row][col] == board[i][j]:  # 짝수 열
                        count += 1
                    elif (col - j) % 2 == 0 and board[row][col] != board[i][j]:  # 홀수 열
                        count += 1
        if count > 64-count:
            count = 64-count
        if count < small:
            small = count
print(small)
