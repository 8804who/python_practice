import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
num = [0] * 100001
attempt = 0
Find = False
q = deque()
q.append(N)
while not Find:
    while len(q) > 0:
        locate = q.popleft()
        if locate == K:
            Find = True
            break
        if 0 <= locate-1 < 100001 and num[locate-1] == 0:
            num[locate-1] = num[locate]+1
            q.append(locate-1)
        if 0 <= locate+1 < 100001 and num[locate+1] == 0:
            num[locate+1] = num[locate]+1
            q.append(locate+1)
        if 0 <= locate*2 < 100001 and num[locate*2] == 0:
            num[locate*2] = num[locate]+1
            q.append(locate*2)
print(num[K])
