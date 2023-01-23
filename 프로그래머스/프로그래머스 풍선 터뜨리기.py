def solution(a):
    answer = 0
    length = len(a)
    arr = [0] * length
    minNum = 1e11
    for i in range(length):
        if minNum > a[i]:
            arr[i] += 1
            minNum = a[i]

    minNum = 1e11
    for i in range(length - 1, -1, -1):
        if minNum > a[i]:
            arr[i] += 1
            minNum = a[i]

    for i in arr:
        if i != 0:
            answer += 1
    return answer