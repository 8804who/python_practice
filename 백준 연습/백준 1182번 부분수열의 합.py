from itertools import combinations
N, S = map(int, input().split())
nums = list(map(int, input().rstrip().split()))
answer = 0
for i in range(1, N+1):
    for j in combinations(nums, i):
        if sum(j) == S:
            answer += 1
print(answer)