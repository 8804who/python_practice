import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
name = {}
unknown = []
count=0
for i in range(N):
    name[sys.stdin.readline().rstrip()] = 1
for i in range(M):
    key = sys.stdin.readline().rstrip()
    try:
        if name[key] == 1:
            count += 1
            unknown.append(key)
    except KeyError:
        continue
print(count)
unknown.sort()
for i in unknown:
    print(i)