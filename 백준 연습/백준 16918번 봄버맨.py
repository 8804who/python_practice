import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())
gameMap = []
second = 1
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque()

for i in range(R):
    gameMap.append(list(sys.stdin.readline().rstrip()))
    for j in range(C):
        if gameMap[i][j] == '.':
            gameMap[i][j] = 3
        else:
            gameMap[i][j] = 1

while second < N:
    for i in range(R):
        for j in range(C):
            if gameMap[i][j] == 0 or gameMap[i][j] == 1:
                gameMap[i][j] += 1
            elif gameMap[i][j] == 2:
                q.append([i, j])
            else:
                gameMap[i][j] = 0
    while q:
        x, y = map(int, q.popleft())
        gameMap[x][y] = 3
        for search in range(4):
            if R > x+move[search][0] >= 0 and C > y+move[search][1] >= 0:
                gameMap[x+move[search][0]][y+move[search][1]] = 3
    second += 1

for i in range(R):
    for j in range(C):
        if gameMap[i][j] == 3:
            print('.', end="")
        else:
            print('O', end="")
    print()
