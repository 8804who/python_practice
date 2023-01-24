import heapq


def solution(N, road, K):
    answer = 0
    roads = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
    distance = [-1] * (N + 1)
    distance[1] = 0
    road.sort(key=lambda x: x[2])
    for i in road:
        if roads[i[0]][i[1]] == -1:
            roads[i[0]][i[1]] = i[2]
            roads[i[1]][i[0]] = i[2]

    heap = []
    for i in range(N + 1):
        if roads[1][i] != -1:
            heapq.heappush(heap, [roads[1][i], i])

    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] == -1:
            distance[node] = dist
        else:
            continue
        for i in range(N + 1):
            if distance[i] == -1 and roads[node][i] != -1:
                heapq.heappush(heap, [dist + roads[node][i], i])

    for i in distance:
        if i != -1 and i <= K:
            answer += 1
    return answer