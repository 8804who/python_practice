from itertools import combinations_with_replacement
N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
for i in combinations_with_replacement(num, M):
    for j in i:
        print(j, end=' ')
    print()
