def solution(n, s, a, b, fares):
    answer = 1e9
    dp = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = 0

    for fare in fares:
        dp[fare[0]][fare[1]] = fare[2]
        dp[fare[1]][fare[0]] = fare[2]

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    for i in range(1, n + 1):
        total = dp[s][i]
        total += dp[i][a]
        total += dp[i][b]
        answer = min(answer, total)
    return answer