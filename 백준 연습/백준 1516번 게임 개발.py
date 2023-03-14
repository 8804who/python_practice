import sys
from collections import deque

N = int(sys.stdin.readline())

need = [0]*(N+1)
dp = [0]*(N+1)
time = [0]*(N+1)
graph = [[] for _ in range(N+1)]
q = deque()

for i in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    time[i+1] = nums[0]
    for j in nums[1:-1]:
        graph[j].append(i+1)
        need[i+1] += 1

for i in range(1, len(need)):
    if need[i] == 0:
        q.append(i)

while q:
    num = q.popleft()
    dp[num] += time[num]
    for i in graph[num]:
        if dp[i] < dp[num]:
            dp[i] = dp[num]
        need[i] -= 1
        if need[i] == 0:
            q.append(i)


for i in range(1, N+1):
    print(dp[i])
