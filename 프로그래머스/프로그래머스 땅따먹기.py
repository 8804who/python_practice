def solution(land):
    length=len(land)
    dp=[[0, 0, 0, 0] for _ in range(length)]
    for i in range(4):
        dp[0][i]=land[0][i]
    for i in range(1,length):
        for j in range(4):
            maxNum=0
            for k in range(4):
                if j==k:
                    continue
                maxNum=max(maxNum, dp[i-1][k])
            dp[i][j]=maxNum+land[i][j]
    return max(dp[length-1])