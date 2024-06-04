import sys
n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
memo = [0] * n
memo[0] = nums[0]
for i in range(1, n):
    if memo[i-1] <= 0:
        memo[i] = nums[i]
    else:
        memo[i] = memo[i-1]+nums[i]

print(max(memo))