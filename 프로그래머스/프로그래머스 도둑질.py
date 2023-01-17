def solution(money):
    answer = 0
    totalmoney = len(money)

    if totalmoney == 1:
        return money[0]

    dp = [0 for _ in range(totalmoney)]

    for i in range(0, totalmoney - 1):
        if i == 0:
            dp[i] = money[i]
        elif i == 1:
            dp[i] = max(dp[i - 1], money[i])
        else:
            dp[i] = max(dp[i - 2] + money[i], dp[i - 1])
    answer = dp[totalmoney - 2]

    for i in range(totalmoney):
        dp[i] = 0

    for i in range(1, totalmoney):
        if i == 1:
            dp[i] = money[i]
        else:
            dp[i] = max(dp[i - 2] + money[i], dp[i - 1])
    if answer < dp[totalmoney - 1]:
        answer = dp[totalmoney - 1]
    return answer