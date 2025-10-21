from collections import deque 
import sys
input = sys.stdin.readline

N = int(input())

cost = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
start_time = [0 for _ in range(N+1)]

q = deque()

for i in range(1, N+1):
    inputs = list(map(int, input().split()))
    cost[i] = inputs[0]

    degrees[i] = inputs[1]

    if inputs[1] == 0:
        q.append([i,inputs[0]])

    for j in range(2,2+inputs[1]):
        graph[inputs[j]].append(i)
    
answer = 0

while q:
    node, end = q.popleft()
    if answer < end:
        answer = end

    for next_node in graph[node]:
        degrees[next_node] -= 1
        if start_time[next_node] < end:
            start_time[next_node] = end
        if degrees[next_node] == 0:
            q.append([next_node, start_time[next_node]+cost[next_node]])
        
print(answer)