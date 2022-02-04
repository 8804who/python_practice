import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(21)] for _ in range(N+1)]
dp[1][num[0]] = 1
for i in range(2, N):
    for j in range(21):
        if 20 >= j+num[i-1] >= 0:
            dp[i][j+num[i-1]] += dp[i-1][j]
        if 20 >= j-num[i-1] >= 0:
            dp[i][j-num[i-1]] += dp[i-1][j]
print(dp[N-1][num[-1]], end="")