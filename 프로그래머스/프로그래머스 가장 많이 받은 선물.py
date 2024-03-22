def solution(friends, gifts):
    answer = 0
    dic = {}
    total = [[0 for _ in range(len(friends) + 1)] for _ in range(len(friends))]

    for i, friend in enumerate(friends):
        dic[friend] = i

    for gift in gifts:
        give, receive = gift.split()
        total[dic[give]][dic[receive]] += 1
        total[dic[give]][-1] += 1
        total[dic[receive]][-1] -= 1

    for i in range(len(friends)):
        count = 0
        for j in range(len(friends)):
            if i == j:
                continue
            if total[i][j] > total[j][i]:
                count += 1
            elif total[i][j] == total[j][i] and total[i][-1] > total[j][-1]:
                count += 1
        if count > answer:
            answer = count
    return answer