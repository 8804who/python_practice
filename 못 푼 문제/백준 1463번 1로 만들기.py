N = int(input())
dp = [0]*(N+1)
for i in range(2, N+1):
    n1 = N
    n2 = N
    n3 = N
    if n1 % 3 == 0:
        n1 //= 3
    if n2 % 2 == 0:
        n2 //= 2
    n3 -= 1
    dp[i] = min(n1, n2, n3)
    print(dp[i])

print(dp[N])