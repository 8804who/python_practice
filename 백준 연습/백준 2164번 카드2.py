from collections import deque
N = int(input())
deq = deque()
for i in range(N, 0, -1):
    deq.append(i)
while len(deq) > 1:
    deq.pop()
    deq.appendleft(deq.pop())
print(deq[0])