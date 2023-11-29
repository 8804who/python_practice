import heapq


def solution(k, n, reqs):
    answer = 1e9
    maximum = n-k+1
    arr = [[0 for _ in range(n-k+2)] for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, maximum+1):
            heap = []
            for req in reqs:
                if req[2] == i:
                    if len(heap) == j:
                        end = heapq.heappop(heap)
                        if req[0] < end:
                            arr[i][j] += end - req[0]
                            heapq.heappush(heap, end+req[1])
                        else:
                            heapq.heappush(heap, req[0]+req[1])
                    else:
                        heapq.heappush(heap, req[0]+req[1])

    queue = [[i, 1, arr[1][i]] for i in range(1, maximum+1)]
    while queue:
        num, idx, time = queue.pop(0)
        if idx == k:
            if answer > time:
                answer = time
        else:
            for i in range(1, maximum+1):
                if num+i <= n:
                    queue.append([num+i, idx+1, time+arr[idx+1][i]])
    return answer