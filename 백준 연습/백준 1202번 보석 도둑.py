import heapq
import sys


def solution(jewels, bags):
    answer = 0
    jewels.sort(reverse=True)
    bags.sort()
    heap = []
    for weight in bags:
        while jewels and jewels[-1][0] <= weight:
            heapq.heappush(heap, -jewels[-1][1])
            jewels.pop()
        if heap:
            answer -= heapq.heappop(heap)
    return answer


input = sys.stdin.readline
N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
print(solution(jewels, bags))