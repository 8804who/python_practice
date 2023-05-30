import sys
N, M = map(int, sys.stdin.readline().split())

room = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
answer = 0

h = 0

while h < N:
    last = -1
    trash = False
    for i in range(M):
        if room[h][i] == 1:
            trash = True
            room[h][i] = 0
            last = i
    h += 1
    if not trash:
        continue
    answer += 1
    for i in range(h, N):
        for j in range(last, M):
            if room[i][j] == 1:
                last = j
            room[i][j] = 0
print(answer)