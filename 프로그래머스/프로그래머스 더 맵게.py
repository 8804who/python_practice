import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new = min1 + min2 * 2
        heapq.heappush(scoville, new)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
    return answer


food = list(map(int, input().split()))
k = int(input())
print(solution(food, k))
