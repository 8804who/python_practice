import sys
A = "0"+sys.stdin.readline().rstrip()
B = "0"+sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(B))] for _ in range(len(A))]
lcs = 0

for a in range(1, len(A)):
    for b in range(1, len(B)):
        if A[a] == B[b]:
            dp[a][b] = dp[a-1][b-1]+1
            if lcs < dp[a][b]:
                lcs = dp[a][b]
        else:
            dp[a][b] = max(dp[a-1][b], dp[a][b-1])
print(lcs)