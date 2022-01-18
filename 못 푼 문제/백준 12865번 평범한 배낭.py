import sys

N, K = map(int, sys.stdin.readline().split())
item = []
maxPrice = 0
bag = [0 for i in range(K+1)]
item.append([0, 0])
for i in range(N):
    item.append(list(map(int, sys.stdin.readline().split())))
item = sorted(item, key=lambda x: x[1])

for i in range(1, N+1):
    for j in range(1, K+1):
        bag[j] = bag[j-1]


print(bag[N][1], end="")
