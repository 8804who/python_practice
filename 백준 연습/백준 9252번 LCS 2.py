import sys
A = '0'+sys.stdin.readline().rstrip()
B = '0'+sys.stdin.readline().rstrip()

x = len(B)-1
y = len(A)-1
string = ''
lcs = 0
dp = [[0 for _ in range(len(B))] for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1]+1
            if lcs < dp[i][j]:
                lcs = dp[i][j]
        else:
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]

while dp[y][x] != 0:
    if dp[y][x] > dp[y-1][x] and dp[y][x] > dp[y][x-1]:
        string += A[y]
        y -= 1
        x -= 1
    else:
        if dp[y-1][x] == dp[y][x]:
            y -= 1
        elif dp[y][x-1] == dp[y][x]:
            x -= 1
print(lcs)
print(string[::-1])