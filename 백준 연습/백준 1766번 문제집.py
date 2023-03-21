import sys
import heapq
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
matters = []
preSolve = [0] * (N+1)
ans = []

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    preSolve[B] += 1

for i in range(1, N+1):
    if preSolve[i] == 0:
        heapq.heappush(matters, i)

while matters:
    idx = heapq.heappop(matters)
    for n in graph[idx]:
        preSolve[n] -= 1
        if preSolve[n] == 0:
            heapq.heappush(matters, n)
    ans.append(idx)
print(*ans)
