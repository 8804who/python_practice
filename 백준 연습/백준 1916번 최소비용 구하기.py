import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

road = [[] for _ in range(N+1)]
distance = [1e9]*(N+1)
heap = []

for i in range(M):
    s, d, c = map(int, sys.stdin.readline().split())
    road[s].append([d, c])

start, destintaion = map(int, sys.stdin.readline().split())
distance[start] = 0

for i in road[start]:
    heapq.heappush(heap, [i[1], i[0]])

while heap:
    dist, city = heapq.heappop(heap)
    if city == destintaion:
        print(dist)
        break
    else:
        for i in road[city]:
            if distance[i[0]] > dist + i[1]:
                heapq.heappush(heap, [dist+i[1], i[0]])
                distance[i[0]] = dist + i[1]