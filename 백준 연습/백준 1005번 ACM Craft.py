import sys
from collections import deque

T = int(sys.stdin.readline())
for t in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))
    need = [0]*(N+1)
    dp = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    q = deque()

    for i in range(K):
        num1, num2 = map(int, sys.stdin.readline().split())
        graph[num1].append(num2)
        need[num2] += 1

    for i in range(1, N+1):
        if need[i] == 0:
            q.append(i)

    W = int(sys.stdin.readline())
    while q:
        num = q.popleft()
        dp[num] += time[num]
        if num == W:
            print(dp[W])
            break
        for n in graph[num]:
            if dp[n] < dp[num]:
                dp[n] = dp[num]
            need[n] -= 1
            if need[n] == 0:
                q.append(n)
