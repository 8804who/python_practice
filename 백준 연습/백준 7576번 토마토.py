import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split(" "))
box = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
unripe = 0
day = 0
queueX = deque()
queueY = deque()
TempX = deque()
TempY = deque()
for i in range(N):
    box[i][:] = map(int, sys.stdin.readline().split())
    for j in range(M):
        if box[i][j] == 0:
            unripe += 1
        if box[i][j] == 1:
            queueX.append(i)
            queueY.append(j)
if unripe > 0:
    while len(queueX) > 0:
        X = queueX.pop()
        Y = queueY.pop()
        for i in range(4):
            if N > X + move[i][0] >= 0 and M > Y + move[i][1] >= 0:
                if not visited[X + move[i][0]][Y + move[i][1]]:
                    visited[X + move[i][0]][Y + move[i][1]] = True
                    if box[X + move[i][0]][Y + move[i][1]] == 1:
                        TempX.append(X + move[i][0])
                        TempY.append(Y + move[i][1])
                    elif box[X + move[i][0]][Y + move[i][1]] == 0:
                        TempX.append(X + move[i][0])
                        TempY.append(Y + move[i][1])
                        unripe -= 1
        if len(queueX) == 0:
            while len(TempX) > 0:
                queueX.append(TempX.pop())
                queueY.append(TempY.pop())
            day += 1
    if unripe > 0:
        print(-1)
    else:
        print(day - 1)
else:
    print(0)