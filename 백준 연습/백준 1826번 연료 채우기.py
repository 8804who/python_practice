import heapq
import sys
N = int(sys.stdin.readline())

arrive = True
count = 0
heap = []
station = [[0, 0]]

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    station.append([a, b])
station.sort()

L, P = map(int, sys.stdin.readline().split())

for i in range(1, N+2):
    if i < N+1:
        P -= station[i][0]-station[i-1][0]
    else:
        P -= L-station[i-1][0]

    while P < 0:
        if not heap:
            arrive = False
            break
        P -= heapq.heappop(heap)
        count += 1
    if i < N+1:
        heapq.heappush(heap, -station[i][1])

if arrive:
    print(count)
else:
    print(-1)