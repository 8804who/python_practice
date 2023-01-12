def solution(elements):
    answer = 0
    check = [0] * (1000 * 1000 + 1)
    elements.insert(0, 0)
    dp = [[0 for _ in range(len(elements))] for _ in range(len(elements))]

    for i in range(1, len(elements)):
        for j in range(1, len(elements)):
            idx = i + j - 1
            if j == 1:
                dp[i][j] = elements[i]
            elif idx < len(elements):
                dp[i][j] = dp[i][j - 1] + elements[idx]
            else:
                dp[i][j] = dp[i][j - 1] + elements[idx - len(elements) + 1]
            if check[dp[i][j]] == 0:
                answer += 1
                check[dp[i][j]] = 1

    return answer