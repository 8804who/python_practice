from collections import deque


def solution(n, info):
    answer = [-1]
    maxScore = 0
    minScore = [0] * 11
    q = deque()
    q.append([n, 0, [0 for _ in range(11)]])

    while q:
        shot, idx, arr = q.pop()

        if idx == 11:
            apeach = 0
            ryan = 0

            if shot > 0:
                arr[10] += shot

            for i in range(11):
                if info[i] == 0 and arr[i] == 0:
                    continue
                if info[i] <= arr[i]:
                    ryan += 10 - i
                else:
                    apeach += 10 - i

            if apeach < ryan and maxScore < ryan - apeach:
                maxScore = ryan - apeach
                minScore = arr
                answer = arr
            elif apeach < ryan and maxScore == ryan - apeach:
                low = True
                for i in range(10, -1, -1):
                    if minScore[i] == arr[i]:
                        continue
                    elif minScore[i] < arr[i]:
                        break
                    else:
                        low = False
                        break
                if low:
                    minScore = arr
                    answer = arr
        else:
            q.append([shot, idx + 1, arr])
            if info[idx] < shot:
                arr2 = [0] * 11
                for i in range(11):
                    arr2[i] = arr[i]
                arr2[idx] += info[idx] + 1
                q.append([shot - arr2[idx], idx + 1, arr2])
    return answer