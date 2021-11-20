import sys
N = int(sys.stdin.readline())
dp = [0]*(N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1]+1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[int(i/2)]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[int(i/3)]+1)
print(dp[N], end="")