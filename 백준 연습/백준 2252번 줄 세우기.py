from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

topology = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    topology[B] += 1

q = deque()

for i in range(1, N+1):
    if topology[i] == 0:
        q.append(i)

while q:
    num = q.popleft()
    print(num, end=' ')
    for next_num in graph[num]:
        topology[next_num] -= 1
        if topology[next_num] == 0:
            q.append(next_num)