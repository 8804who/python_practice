import sys


def TSP(now, visited):
    if visited == (1 << N)-1:
        if expenses[now][0] != 0:
            return expenses[now][0]
        else:
            return 1e9

    if dp[now][visited] != 0:
        return dp[now][visited]

    dp[now][visited] = 1e9

    for i in range(N):
        if visited & (1 << i):
            continue
        if expenses[now][i] == 0:
            continue
        temp = TSP(i, visited | 1 << i)
        dp[now][visited] = min(dp[now][visited], expenses[now][i]+temp)
    return dp[now][visited]


input = sys.stdin.readline
N = int(input())
dp = [[0 for _ in range(1 << N)] for _ in range(N)]
expenses = [list(map(int, input().rstrip().split())) for _ in range(N)]
print(TSP(0, 1))
