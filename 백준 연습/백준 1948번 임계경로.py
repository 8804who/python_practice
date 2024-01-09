from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
reversed_graph = [[] for _ in range(n+1)]
routes = [0] * (n+1)

for _ in range(m):
    start, destination, time = map(int, input().split())
    graph[start].append([destination, time])
    reversed_graph[destination].append([start, time])
    routes[destination] += 1

start, destination = map(int, input().split())

q = deque([[start, 0]])
routes[start] = 1
longest_time = [0] * (n+1)

while q:
    city, time = q.popleft()
    if longest_time[city] < time:
        longest_time[city] = time
    routes[city] -= 1
    if routes[city] == 0:
        for d, t in graph[city]:
            q.append([d, longest_time[city]+t])

q = deque([[destination, longest_time[destination]]])
count = 0
visits = [False] * (n+1)

while q:
    city, time = q.popleft()
    for s, t in reversed_graph[city]:
        if time-t == longest_time[s]:
            count += 1
            if not visits[s]:
                q.append([s, time-t])
                visits[s] = True

print(longest_time[destination], count, sep='\n')