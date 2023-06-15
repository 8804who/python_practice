from collections import deque
import heapq
import sys


def check_shortest_path(s, d):
    global shortest_paths
    global shortest

    q = deque()
    q.append(d)
    while q:
        node = q.popleft()

        if node == s:
            continue

        for road in reverse_roads[node]:
            key = str(road[0])+'-'+str(node)
            if shortest[road[0]] + road[1] == shortest[node] and key not in shortest_paths:
                shortest_paths[key] = -1
                q.append(road[0])


while True:
    N, M = map(int, sys.stdin.readline().split())
    if M == 0:
        break
    S, D = map(int, sys.stdin.readline().split())

    global shortest
    global shortest_paths

    roads = [[] for _ in range(N)]
    reverse_roads = [[] for _ in range(N)]
    shortest = [-1 for _ in range(N)]
    shortest_paths = {}

    shortest[S] = 0

    for i in range(M):
        U, V, P = map(int, sys.stdin.readline().split())
        roads[U].append((V, P))
        reverse_roads[V].append((U, P))

    heap = []
    for road in roads[S]:
        heapq.heappush(heap, [road[1], road[0]])

    while heap:
        cost, now = heapq.heappop(heap)
        if shortest[now] != -1:
            continue
        shortest[now] = cost
        for road in roads[now]:
            heapq.heappush(heap, ([cost+road[1], road[0]]))

    check_shortest_path(S, D)

    shortest = [-1 for _ in range(N)]
    heap = []

    for road in roads[S]:
        key = str(S)+'-'+str(road[0])
        if key not in shortest_paths:
            heapq.heappush(heap, [road[1], road[0]])

    while heap:
        cost, now = heapq.heappop(heap)
        if shortest[now] != -1:
            if now == D:
                break
            continue
        shortest[now] = cost

        for road in roads[now]:
            key = str(now) + '-' + str(road[0])
            if key not in shortest_paths:
                heapq.heappush(heap, [cost+road[1], road[0]])
    print(shortest[D])