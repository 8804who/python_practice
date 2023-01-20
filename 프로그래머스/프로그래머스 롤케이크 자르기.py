def solution(topping):
    answer = 0
    length = len(topping)
    cut = 0
    old = {}
    young = {}

    for i in topping:
        if i in young:
            young[i] += 1
        else:
            young[i] = 1

    while cut < length:
        if topping[cut] in old:
            old[topping[cut]] += 1
        else:
            old[topping[cut]] = 1

        if young[topping[cut]] > 1:
            young[topping[cut]] -= 1
        else:
            del young[topping[cut]]

        if len(old) == len(young):
            answer += 1
        cut += 1
    return answer