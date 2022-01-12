import sys
N, M = map(int, sys.stdin.readline().split())
loadMap = []
count = 0
for i in range(N):
    loadMap.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    runway = [0 for _ in range(N)]
    canThrough = True
    for j in range(N-1):
        if loadMap[i][j] == loadMap[i][j+1]:
            pass
        elif loadMap[i][j]-loadMap[i][j+1] == -1 and runway[j] == 0:
            n = 0
            while n <= M-1:
                if j - n < 0:
                    canThrough = False
                    break
                if loadMap[i][j] != loadMap[i][j - n] or runway[j - n] == 1:
                    canThrough = False
                    break
                if n == M-1:
                    n2 = 0
                    while n2 < M:
                        runway[j - n2] = 1
                        n2 += 1
                n += 1

        elif loadMap[i][j]-loadMap[i][j+1] == 1 and runway[j+1] == 0:
            n = 1
            while n <= M:
                if j + n >= N:
                    canThrough = False
                    break
                if loadMap[i][j + 1] != loadMap[i][j + n]:
                    canThrough = False
                    break
                if n == M:
                    n2 = 0
                    while n2 < M:
                        n2 += 1
                        runway[j + n2] = 1
                n += 1
        else:
            canThrough = False
            break
    if canThrough:
        count += 1

for i in range(N):
    runway = [0 for _ in range(N)]
    canThrough = True
    for j in range(N-1):
        if loadMap[j][i] == loadMap[j+1][i]:
            pass
        elif loadMap[j][i]-loadMap[j+1][i] == -1 and runway[j] == 0:
            n = 0
            while n <= M-1:
                if j - n < 0:
                    canThrough = False
                    break
                if loadMap[j][i] != loadMap[j-n][i] or runway[j - n] == 1:
                    canThrough = False
                    break
                if n == M-1:
                    n2 = 0
                    while n2 < M:
                        runway[j - n2] = 1
                        n2 += 1
                n += 1

        elif loadMap[j][i]-loadMap[j+1][i] == 1 and runway[j+1] == 0:
            n = 1
            while n <= M:
                if j + n >= N:
                    canThrough = False
                    break
                if loadMap[j+1][i] != loadMap[j+n][i]:
                    canThrough = False
                    break
                if n == M:
                    n2 = 0
                    while n2 < M:
                        n2 += 1
                        runway[j + n2] = 1
                n += 1
        else:
            canThrough = False
            break
    if canThrough:
        count += 1
print(count)