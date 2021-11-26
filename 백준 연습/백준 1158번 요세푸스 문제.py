import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
q = deque()
num = []
for i in range(N):
    q.append(i + 1)
count = 0
print("<", end="")
while len(q) > 1:
    count += 1
    if count == K:
        print(q.popleft(), ",", sep="", end=" ")
        count = 0
    else:
        q.append(q.popleft())
print(q.popleft(), ">", sep="", end=" ")