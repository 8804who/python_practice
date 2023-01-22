def solution(weights):
    answer = 0
    arr = [0] * 1001
    for i in weights:
        arr[i] += 1

    for i in range(1001):
        for j in [1, 3 / 2, 2, 4 / 3]:
            num = int(i * j)
            if i * j != num:
                continue
            if num < 1001:
                if num == i:
                    if arr[i] > 1:
                        answer += (arr[i] * (arr[i] - 1)) // 2
                else:
                    answer += arr[i] * arr[num]
    return answer