from itertools import permutations
N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
for i in permutations(num, M):
    for j in i:
        print(j, end=' ')
    print()
