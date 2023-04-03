import sys
import heapq

while True:
    N, A, B = map(int, sys.stdin.readline().split())
    if N == 0:
        break
    balloon = [A, B]
    dist = [[0, 0] for _ in range(N)]
    heap = []
    total = 0

    for i in range(N):
        K, dA, dB = map(int, sys.stdin.readline().split())
        dist[i] = [dA, dB]
        diff = (dA-dB)**2
        heapq.heappush(heap, [-diff, K, i])

    while heap:
        d, k, idx = heapq.heappop(heap)
        biggerB = dist[idx][0] < dist[idx][1]
        if balloon[not biggerB] >= k:
            balloon[not biggerB] -= k
            total += k*dist[idx][not biggerB]
        elif balloon[not biggerB] > 0:
            k -= balloon[not biggerB]
            total += balloon[not biggerB]*dist[idx][not biggerB]
            balloon[not biggerB] = 0
            total += k*dist[idx][biggerB]
            balloon[biggerB] -= k
        else:
            total += k * dist[idx][biggerB]
            balloon[biggerB] -= k
    print(total)