from collections import deque


def solution(enroll, referral, seller, amount):
    answer = []
    sell = {}
    ref = {}

    q = deque()
    for e in enroll:
        sell[e] = 0

    for i in range(len(referral)):
        if referral[i] == '-':
            continue
        else:
            ref[enroll[i]] = referral[i]

    for i in range(len(seller)):
        q.append(i)

    while q:
        idx = q.popleft()
        name = seller[idx]
        price = amount[idx] * 100
        while True:
            if price >= 10:
                fee = price // 10
                price -= fee
            else:
                sell[name] += price
                break
            sell[name] += price
            price = fee
            if name not in ref:
                break
            else:
                name = ref[name]

    for i in sell:
        answer.append(sell[i])
    return answer