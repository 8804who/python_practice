import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range(N+1)]

for n in num:
    dp[n] = dp[n-1]+1
print(N-max(dp))