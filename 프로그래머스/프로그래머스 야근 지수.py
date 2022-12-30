import heapq


def solution(n, works):
    if n >= sum(works):
        return 0
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap, -work)

    for i in range(n):
        num = -heapq.heappop(heap)
        num -= 1
        heapq.heappush(heap, -num)

    for i in heap:
        answer += i ** 2
    return answer