import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
start = list(map(int, sys.stdin.readline().rstrip().split()))
end = {i: e for e, i in enumerate(list(map(int, sys.stdin.readline().rstrip().split())))}

switchs = [end[s] for s in start]

lis = [switchs[0]]
idx = [0]

for switch in switchs[1:]:
    if switch > lis[-1]:
        idx.append(len(lis))
        lis.append(switch)
    else:
        temp = bisect_left(lis, switch)
        idx.append(temp)
        lis[temp] = switch

n = len(lis)-1
answer = []
for a, i in zip(range(N-1, -1, -1), idx[::-1]):
    if i == n:
        answer.append(start[a])
        n -= 1
print(len(lis))
print(*sorted(answer))