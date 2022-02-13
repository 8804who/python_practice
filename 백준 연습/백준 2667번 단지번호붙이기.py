import sys
from collections import deque
N = int(sys.stdin.readline())
townMap = []
visited = [[False for _ in range(N)]for _ in range(N)]
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque()
estate = 0

for i in range(N):
    townMap.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(N):
    for j in range(N):
        if not visited[i][j] and townMap[i][j] == 1:
            q.append([i, j])
            estate += 1
        while q:
            x, y = q.popleft()
            townMap[x][y] = estate
            for m in range(4):
                if N > x+move[m][0] >= 0 and N > y+move[m][1] >= 0:
                    if townMap[x+move[m][0]][y+move[m][1]] == 1 and not visited[x+move[m][0]][y+move[m][1]]:
                        visited[x+move[m][0]][y+move[m][1]] = True
                        q.append([x+move[m][0], y+move[m][1]])

print(estate)
count = [0 for i in range(estate)]
for i in range(N):
    for j in range(N):
        if townMap[i][j] != 0:
            count[townMap[i][j]-1] += 1
count.sort()
for i in count:
    print(i)
