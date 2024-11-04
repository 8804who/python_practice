import sys
sys.setrecursionlimit(1000000)


def match(worker):
    for work in works[worker]:
        if done[work]:
            continue
        done[work] = True
        if assign[work] == -1 or match(assign[work]):
            assign[work] = worker
            return True
    return False


N, M = map(int, sys.stdin.readline().split())
done = [False] * (N+1)
assign = [-1] * (N+1)

dist = [[1,N] for _ in range(N+1)]
arr_min = [1] * (N+1)
arr_max = [N] * (N+1)

works = [[] for _ in range(N+1)]

for _ in range(M):
    a, x, y, v = map(int, sys.stdin.readline().split())

    if dist[v][0] < x:
        dist[v][0] = x
    if dist[v][1] > y:
        dist[v][1] = y

    for i in range(x, y+1):
        if a == 1:
            if arr_max[i] > v:
                arr_max[i] = v
        else:
            if arr_min[i] < v:
                arr_min[i] = v

for i in range(1,N+1):
    for j in range(dist[i][0], dist[i][1]+1):
        if arr_min[j]<=i<=arr_max[j]:
            works[i].append(j)

pos = 0

for i in range(1,N+1):
    done = [False] * (N+1)
    if match(i):
        pos += 1

if pos == N:
    print(*assign[1:])
else:
    print(-1)