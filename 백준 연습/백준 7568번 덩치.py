import sys
n = int(sys.stdin.readline())
bulk = []
for i in range(n):
    bulk.append([])
    weight, height = map(int, sys.stdin.readline().split())
    bulk[i].append(weight)
    bulk[i].append(height)
for i in range(n):
    count = 1
    for j in range(n):
        if bulk[i][0] < bulk[j][0] and bulk[i][1] < bulk[j][1]:
            count += 1
    print(count, end=" ")