def solution(n):
    dp = [1] * (n+1)
    for i in range(2, n+1, 2):
        dp[i] = dp[i-2]*3
        for j in range(4, i+1, 2):
            dp[i] += dp[i-j]*2
    return dp[n] % 1000000007