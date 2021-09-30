import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
deq = deque([i for i in range(1, N+1)])
print("<", end="")
for i in range(N-1):
    for j in range(K):
        deq.append(deq.popleft())
    print(deq.pop(), end=", ")
print(deq.pop(), end=">")
