def solution(n, results):
    answer = 0
    win = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    lost = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for result in results:
        winner = result[0]
        loser = result[1]

        win[winner][loser] = 1
        lost[loser][winner] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if win[j][i] == 1 and win[i][k] == 1:
                    win[j][k] = 1
                if lost[j][i] == 1 and lost[i][k] == 1:
                    lost[j][k] = 1

    for i in range(1, n + 1):
        if sum(win[i]) + sum(lost[i]) == n - 1:
            answer += 1
    return answer