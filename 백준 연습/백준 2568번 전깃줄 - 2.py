import bisect
import sys
input = sys.stdin.readline
N = int(input())
line = []

for i in range(N):
    line.append(list(map(int, input().rstrip().split())))
line.sort()

record = [0]
lis = [line[0][1]]

for s, d in line[1:]:
    if d > lis[-1]:
        lis.append(d)
        record.append(len(lis)-1)
    else:
        idx = bisect.bisect_left(lis, d)
        lis[idx] = d
        record.append(idx)

idx = len(lis)-1
remove = []
for i, rec in zip(range(N-1, -1, -1), record[::-1]):
    if rec == idx:
        idx -= 1
    else:
        remove.append(line[i][0])
print(len(remove))
for r in remove[::-1]:
    print(r)