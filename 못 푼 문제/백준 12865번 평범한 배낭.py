import sys

N, K = map(int, sys.stdin.readline().split())
item = []
maxPrice = 0
bag = [[0, 0] for i in range(N+1)]
item.append([0, 0])
for i in range(N):
    item.append(list(map(int, sys.stdin.readline().split())))
item = sorted(item, key=lambda x: x[1])

for i in range(1, N+1):
    bag[i][0] = bag[i - 1][0]
    bag[i][1] = bag[i - 1][1]
    if bag[i][0] + item[i][0] <= K:
        bag[i][0] += item[i][0]
        bag[i][1] += item[i][1]
    else:
        for j in range(i-1, -1):
            if bag[j][0]+item[i][0] <= K:
                if bag[j][1]+item[i][1] > bag[i][1]:
                    bag[i][0] = bag[j][0]+item[i][0]
                    bag[i][1] = bag[j][1]+item[i][1]
print(bag[N][1], end="")
