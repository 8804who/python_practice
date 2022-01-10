import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())

Lab = [[0 for j in range(w+1)] for i in range(h+1)]
visited = [[False for _ in range(w+1)]for _ in range(h+1)]
virusLocation = []
blankLocation = []

virus = deque()
blank = deque()

move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
maxCount = 0

for i in range(1, h+1):
    inputMap = list(map(int, sys.stdin.readline().split()))
    for j in range(1, w+1):
        Lab[i][j] = inputMap[j-1]
        if Lab[i][j] == 2:
            virusLocation.append([i, j])
        elif Lab[i][j] == 0:
            blankLocation.append([i, j])

for h1 in range(len(blankLocation)):
    Lab[blankLocation[h1][0]][blankLocation[h1][1]] = 1
    for h2 in range(h1+1, len(blankLocation)):
        Lab[blankLocation[h2][0]][blankLocation[h2][1]] = 1
        for h3 in range(h2+1, len(blankLocation)):
            Lab[blankLocation[h3][0]][blankLocation[h3][1]] = 1
            for i in range(len(virusLocation)):
                virus.append(virusLocation[i])
            count = 0

            while len(virus) > 0:
                location = virus.popleft()
                x = location[0]
                y = location[1]
                for i in range(4):
                    if 0 < x+move[i][0] <= h and 0 < y+move[i][1] <= w:
                        if Lab[x+move[i][0]][y+move[i][1]] == 0 and not visited[x+move[i][0]][y+move[i][1]]:
                            visited[x+move[i][0]][y+move[i][1]] = True
                            Lab[x+move[i][0]][y+move[i][1]] = 2
                            virus.append([x+move[i][0], y+move[i][1]])
                            blank.append([x+move[i][0], y+move[i][1]])
            for i in range(1, h+1):
                for j in range(1, w+1):
                    visited[i][j] = False
                    if Lab[i][j] == 0:
                        count += 1

            Lab[blankLocation[h3][0]][blankLocation[h3][1]] = 0

            while len(blank) > 0:
                location = blank.popleft()
                Lab[location[0]][location[1]] = 0

            maxCount = max(count, maxCount)
        Lab[blankLocation[h2][0]][blankLocation[h2][1]] = 0
    Lab[blankLocation[h1][0]][blankLocation[h1][1]] = 0
print(maxCount, end="")