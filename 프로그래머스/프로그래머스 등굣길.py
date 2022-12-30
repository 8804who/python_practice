def solution(m, n, puddles):
    road = [[0 for _ in range(m)] for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    move = [[-1, 0], [0, -1]]

    for puddle in puddles:
        road[puddle[1] - 1][puddle[0] - 1] = 1

    dp[0][0] = 1

    for x in range(n):
        for y in range(m):
            if road[x][y] == 0:
                for i in range(2):
                    prevX, prevY = x + move[i][0], y + move[i][1]
                    if n > prevX and prevX >= 0 and m > prevY and prevY >= 0:
                        dp[x][y] += dp[prevX][prevY] % 1000000007
                        dp[x][y] %= 1000000007

    return dp[n - 1][m - 1]