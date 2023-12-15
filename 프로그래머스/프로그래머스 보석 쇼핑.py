def solution(gems):
    answer = [1, len(gems)]

    inven = {gem: 0 for gem in set(gems)}
    start, end = 0, 0
    inven[gems[0]] += 1
    need_type = len(inven) - 1

    while end < len(gems):
        if need_type == 0 and answer[1] - answer[0] > end - start:
            answer = start + 1, end + 1

        if inven[gems[start]] > 1:
            inven[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end < len(gems):
                inven[gems[end]] += 1
                if inven[gems[end]] == 1:
                    need_type -= 1
    return answer