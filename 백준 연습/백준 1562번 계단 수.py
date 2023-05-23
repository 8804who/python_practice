N = int(input())
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N+1)]

for n in range(10):
    dp[1][n][1 << n] = 1

for i in range(1, N):
    for n in range(10):
        for k in range(1024):
            if n == 0:
                dp[i+1][1][k | 1 << 1] += dp[i][n][k]
            elif n == 9:
                dp[i+1][8][k | 1 << 8] += dp[i][n][k]
            else:
                dp[i+1][n-1][k | 1 << (n-1)] += dp[i][n][k]
                dp[i+1][n+1][k | 1 << (n+1)] += dp[i][n][k]


answer = 0
for i in range(1, 10):
    answer += dp[N][i][1023]
print(answer % 1000000000)