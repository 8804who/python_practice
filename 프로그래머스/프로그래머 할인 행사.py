def solution(want, number, discount):
    answer = 0
    item = {}
    for i in range(10):
        if discount[i] in item:
            item[discount[i]] += 1
        else:
            item[discount[i]] = 1

    if check(want, item, number):
        answer += 1

    for i in range(len(discount) - 10):
        if item[discount[i]] == 1:
            del item[discount[i]]
        else:
            item[discount[i]] -= 1
        if discount[i + 10] in item:
            item[discount[i + 10]] += 1
        else:
            item[discount[i + 10]] = 1
        if check(want, item, number):
            answer += 1
    return answer


def check(w, i, n):
    for j in range(len(w)):
        if w[j] not in i or n[j] != i[w[j]]:
            return False
    return True