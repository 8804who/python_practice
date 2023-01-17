def solution(sticker):
    answer = 0
    totalSticker = len(sticker)

    if totalSticker == 1:
        return sticker[0]

    dp = [0 for _ in range(totalSticker)]

    for i in range(0, totalSticker - 1):
        if i == 0:
            dp[i] = sticker[i]
        elif i == 1:
            dp[i] = max(dp[i - 1], sticker[i])
        else:
            dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    answer = dp[totalSticker - 2]

    for i in range(totalSticker):
        dp[i] = 0

    for i in range(1, totalSticker):
        if i == 1:
            dp[i] = sticker[i]
        else:
            dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    if answer < dp[totalSticker - 1]:
        answer = dp[totalSticker - 1]
    return answer