from itertools import combinations
N, M = map(int, input().split())
num = [i for i in range(1, N+1)]
for i in combinations(num, M):
    for j in i:
        print(j, end=' ')
    print()