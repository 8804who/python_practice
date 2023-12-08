def solution(e, starts):
    counts = [0] * (e + 1)

    for i in range(2, e + 1):
        for j in range(1, min(e // i + 1, i)):
            counts[i * j] += 2
    for i in range(1, int(e ** (1 / 2)) + 1):
        counts[i * i] += 1

    max_count = -1
    dp = [0] * (e + 1)
    for i in range(e, 0, -1):
        if counts[i] >= max_count:
            max_count = counts[i]
            dp[i] = i
        else:
            dp[i] = dp[i + 1]

    return [dp[start] for start in starts]