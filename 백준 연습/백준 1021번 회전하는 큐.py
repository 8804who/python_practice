from collections import deque
N, M = map(int, input().split())
q = deque()
for i in range(1, N+1):
    q.append(i)
popList = list(map(int, input().split()))
num = 0
count = 0
while num < M:
    where = q.index(popList[num])
    if where == 0:
        q.popleft()
        num += 1
    elif where < len(q)/2:
        q.append(q.popleft())
        count += 1
    else:
        q.appendleft(q.pop())
        count += 1
print(count, end="")