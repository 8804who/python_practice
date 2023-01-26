import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

road = [[1e9 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    s, d, c = map(int, sys.stdin.readline().split())
    if road[s][d] > c:
        road[s][d] = c

for i in range(n+1):
    road[i][i]=0

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if road[i][j] > road[i][k]+road[k][j]:
                road[i][j] = road[i][k]+road[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if road[i][j] != 1e9:
            print(road[i][j], end=' ')
        else:
            print(0, end=' ')
    print()