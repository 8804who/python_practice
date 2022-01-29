import sys
price = []
dp = []
minSum = 1000000
for i in range(int(sys.stdin.readline())):
    price.append(list(map(int, sys.stdin.readline().split())))
for i in range(len(price)):
    dp.append([])
    for j in range(3):
        dp[i].append(price[i][j])
        if i > 0:
            if j == 0:
                dp[i][j] += min(dp[i-1][1], dp[i-1][2])
            elif j == 1:
                dp[i][j] += min(dp[i-1][0], dp[i-1][2])
            else:
                dp[i][j] += min(dp[i-1][0], dp[i-1][1])
        if i == len(price)-1:
            minSum = min(minSum, dp[i][j])
print(minSum, end="")