import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
q = deque()
num = []
for i in range(N):
    q.append(i+1)
count = 0
while q:
    count += 1
    if count == K:
        num.append(q.popleft())
        count = 0
    else:
        q.append(q.popleft())
print("<", end="")
for i in range(N-1):
    print(num[i], ",", sep="", end=" ")
print(num[N-1], ">", sep="", end=" ")