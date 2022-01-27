import sys

N, K = map(int, sys.stdin.readline().split())
item = []
maxPrice = 0
bag = [[0 for _ in range(K+1)] for _ in range(N+1)]
item.append([0, 0])
for i in range(N):
    item.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        if item[i][0] <= j:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-item[i][0]]+item[i][1])
        else:
            bag[i][j] = bag[i-1][j]
        if bag[i][j] > maxPrice:
            maxPrice = bag[i][j]
print(maxPrice, end="")
