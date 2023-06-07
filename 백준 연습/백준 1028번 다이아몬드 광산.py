import sys
R, C = map(int, sys.stdin.readline().split())

arr = [sys.stdin.readline().rstrip() for _ in range(R)]
up = [[0 for _ in range(C)] for _ in range(R)]
down = [[0 for _ in range(C)] for _ in range(R)]
answer = 0

for i in range(C):
    if arr[R-1][i] == '1':
        up[R-1][i] = 1
    if arr[0][i] == '1':
        down[0][i] = 1

for i in range(R-2, -1, -1):
    for j in range(C):
        if arr[i][j] == '1':
            if j == 0:
                up[i][j] = 1
            else:
                up[i][j] = up[i+1][j-1]+1

for i in range(1, R):
    for j in range(C):
        if arr[i][j] == '1':
            if j == 0:
                down[i][j] = 1
            else:
                down[i][j] = down[i-1][j-1]+1

for i in range(R):
    for j in range(C):
        for k in range(up[i][j], -1, -1):
            if answer >= k+1:
                break
            if i+k < R and j+k < C and i+2*k < R:
                if up[i+k][j+k] >= k+1 and down[i+k][j+k] >= k+1 and down[i+2*k][j] >= k+1:
                    answer = k+1
print(answer)
