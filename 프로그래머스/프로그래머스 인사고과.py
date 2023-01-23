def solution(scores):
    answer = 0
    length = len(scores)
    fail = [False for _ in range(length)]

    for i in range(length):
        scores[i].append(i)
    scores.sort(key=lambda x: (x[0], x[1]))

    nowAttitude = scores[-1][0]
    prevMax = -1
    maxPeer = scores[-1][1]

    for i in range(length - 1, -1, -1):
        if nowAttitude != scores[i][0]:
            if prevMax < maxPeer:
                prevMax = maxPeer
            nowAttitude = scores[i][0]
            maxPeer = scores[i][1]
        if prevMax > scores[i][1]:
            fail[scores[i][2]] = True

    scores.sort(key=lambda x: (x[0] + x[1], -x[2]), reverse=True)

    if fail[0]:
        return -1

    for i in scores:
        if i[2] == 0:
            answer += 1
            break
        else:
            if fail[i[2]]:
                continue
            else:
                answer += 1
    return answer