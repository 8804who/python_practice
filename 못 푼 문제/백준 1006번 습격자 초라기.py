import sys

T = int(sys.stdin.readline())

for test_case in range(T):
    N, W = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0 for _ in range(N)] for _ in range(2)]

    for i in range(2):
        for j in range(N):
            if arr[i][j]+arr[(i+1)%2][j] <= W:
                dp[i][j] += 1
            if arr[i][j-1]+arr[i][j] <= W:
                dp[i][j] += 1
            if arr[i][(j+1)%N]+arr[i][j] <= W:
                dp[i][j] += 1

    for i in range(2):
        for j in range(N):
            if dp[i][j] < 0:
                continue
            if arr[i][j]+arr[(i+1)%2][j] <= W:
                if (dp[(i+1)%2][j] == 1 and dp[i][j] > -1) or (dp[(i+1)%2][j] > -1 and dp[i][j] == 1):
                    dp[(i+1)%2][j] = 0
                    dp[i][j] = -1
                dp[(i+1)%2][j] -= 1
            if arr[i][j-1]+arr[i][j] <= W:
                if (dp[i][j-1] == 1 and dp[i][j] > -1) or (dp[i][j-1] > -1 and dp[i][j] == 1):
                    dp[i][j-1] = 0
                    dp[i][j] = -1
                dp[i][j-1] -= 1
            if arr[i][(j+1)%N]+arr[i][j] <= W:
                if (dp[i][(j+1)%N] == 1 and dp[i][j] > -1) or (dp[i][(j+1)%N] > -1 and dp[i][j] == 1):
                    dp[i][(j+1)%N] = 0
                    dp[i][j] = -1
                dp[i][(j+1)%N] -= 1

    count = 0
    for i in range(2):
        for j in range(N):
            if dp[i][j] > -1:
                count += 1
    count += (N*2-count)//2
    print(count)
