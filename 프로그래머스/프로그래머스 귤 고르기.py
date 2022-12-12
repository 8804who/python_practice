def solution(k, tangerine):
    size = [0 for _ in range(10000001)]
    for orange in tangerine:
        size[orange] += 1
    size.sort(reverse=True)

    answer = 0
    num = 0
    for orange in size:
        num += orange
        answer += 1
        if num >= k:
            break

    return answer