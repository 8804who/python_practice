from collections import deque

def solution(stones, k):
    q = deque()
    for idx in range(k):
        while q and q[-1][0]<=stones[idx]:
            q.pop()
        q.append([stones[idx], idx])

    for idx in range(k, len(stones)):
        stones[idx] = min(q[0][0], stones[idx])
        if q[0][1] == idx-k:
            q.popleft()
        while q and q[-1][0]<=stones[idx]:
            q.pop()
        q.append([stones[idx], idx])

    return q[0][0]