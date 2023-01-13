import math


def solution(n, stations, w):
    answer = 0

    s = 1
    for i in stations:
        answer += math.ceil((i - w - s) / (w * 2 + 1))
        s = i + w + 1
    if n > s:
        answer += math.ceil((n - s) / (w * 2 + 1))
    if n == s:
        answer += 1
    return answer