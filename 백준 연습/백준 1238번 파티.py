import heapq
import sys


def getDistance(route, node):
    heap = []
    time = [-1 for _ in range(N+1)]
    time[node] = 0
    for i in range(N+1):
        if route[node][i] != 101:
            heapq.heappush(heap, [route[X][i], i])

    while heap:
        t, d = heapq.heappop(heap)
        if time[d] == -1:
            time[d] = t
        else:
            continue
        for i in range(N+1):
            if time[i] == -1 and route[d][i] != 101:
                heapq.heappush(heap, [t+route[d][i], i])
    return time


N, M, X = map(int, sys.stdin.readline().split())

to_party = [[101 for _ in range(N+1)] for _ in range(N+1)]
to_home = [[101 for _ in range(N+1)] for _ in range(N+1)]
maxTime = -1

for m in range(M):
    s, d, t = map(int, sys.stdin.readline().split())
    to_party[s][d] = min(to_party[s][d], t)
    to_home[d][s] = min(to_home[d][s], t)

go_time = getDistance(to_party, X)
back_time = getDistance(to_home, X)

for i in range(N+1):
    if maxTime < go_time[i]+back_time[i]:
        maxTime = go_time[i]+back_time[i]
print(maxTime)
