import sys
from collections import deque

N = int(sys.stdin.readline())
gameMap = [[0 for j in range(N)] for i in range(N)]

K = int(sys.stdin.readline())
for i in range(K):
    H, W = map(int, sys.stdin.readline().split())
    gameMap[H-1][W-1] = 1

L = int(sys.stdin.readline())
changeDircetion = []
for i in range(L):
    T, W = map(str, sys.stdin.readline().split())
    changeDircetion.append([int(T), W])

snakesBodyX = deque()
snakesBodyY = deque()
direction = 'D'
time = 0
bodyLength = 1
gameOver = False
directionChangeTime = 0
directionXY = [[-1, 0], [1, 0], [0, -1], [0, 1]]

snakesBodyX.append(0)
snakesBodyY.append(0)

while not gameOver:
    time += 1
    if direction == 'D':
        headLocationX = snakesBodyX[-1] + directionXY[3][0]
        headLocationY = snakesBodyY[-1] + directionXY[3][1]

    elif direction == 'L':
        headLocationX = snakesBodyX[-1] + directionXY[2][0]
        headLocationY = snakesBodyY[-1] + directionXY[2][1]

    elif direction == 'U':
        headLocationX = snakesBodyX[-1] + directionXY[0][0]
        headLocationY = snakesBodyY[-1] + directionXY[0][1]

    else:
        headLocationX = snakesBodyX[-1] + directionXY[1][0]
        headLocationY = snakesBodyY[-1] + directionXY[1][1]

    if 0 > headLocationX or headLocationX >= N or 0 > headLocationY or headLocationY >= N:
        gameOver = True
        break

    for i in range(bodyLength):
        tempX = snakesBodyX.popleft()
        tempY = snakesBodyY.popleft()
        if tempX == headLocationX and tempY == headLocationY:
            gameOver = True
            break
        snakesBodyX.append(tempX)
        snakesBodyY.append(tempY)

    snakesBodyX.append(headLocationX)
    snakesBodyY.append(headLocationY)

    if gameMap[snakesBodyX[-1]][snakesBodyY[-1]] != 1:
        snakesBodyX.popleft()
        snakesBodyY.popleft()
    else:
        bodyLength += 1
        gameMap[snakesBodyX[-1]][snakesBodyY[-1]] = 0

    if time == changeDircetion[directionChangeTime][0]:
        if changeDircetion[directionChangeTime][1] == 'D':
            if direction == 'D':
                direction = 'B'
            elif direction == 'L':
                direction = 'U'
            elif direction == 'B':
                direction = 'L'
            else:
                direction = 'D'
        else:
            if direction == 'D':
                direction = 'U'
            elif direction == 'L':
                direction = 'B'
            elif direction == 'B':
                direction = 'D'
            else:
                direction = 'L'
        if directionChangeTime < L-1:
            directionChangeTime += 1
print(time)