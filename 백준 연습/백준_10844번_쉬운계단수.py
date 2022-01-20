n = int(input())
memo = [[0 for _ in range(10)] for _ in range(n)]
for i in range(10):
    memo[0][i] = 1
for i in range(1, n):
    memo[i][0] = memo[i-1][1]
    for j in range(1, 9):
        memo[i][j] = memo[i-1][j-1]+memo[i-1][j+1]
    memo[i][9] = memo[i-1][8]
print(sum(memo[n-1][1:]) % 1000000000, end="")
