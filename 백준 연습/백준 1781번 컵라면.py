import sys
import heapq

N = int(sys.stdin.readline())
problems = [[] for _ in range(N+1)]
heap = []

for i in range(N):
    d, p = list(map(int, sys.stdin.readline().split()))
    problems[d].append(p)

time = N
answer = 0
while time > 0:
    for problem in problems[time]:
        heapq.heappush(heap, -problem)
    answer -= heapq.heappop(heap) if heap else 0
    time -= 1
print(answer)