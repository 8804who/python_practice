import sys
memo = [[[False for _ in range(51)] for _ in range (51)] for _ in range (51)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        if not memo[20][20][20]:
            memo[20][20][20] = w(20, 20, 20)
        return memo[20][20][20]
    elif a < b < c:
        if not memo[a][b][c]:
            memo[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return memo[a][b][c]
    else:
        if not memo[a][b][c]:
            memo[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return memo[a][b][c]


while True:
    A, B, C = map(int, sys.stdin.readline().split())
    if A == B == C == -1:
        break
    print("w(", A, ", ", B, ", ", C, ") = ", w(A, B, C), sep="")
