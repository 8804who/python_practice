from itertools import product


def solution(users, emoticons):
    maxRegist = 0
    maxPrice = 0
    for i in range(len(emoticons)):
        emoticons[i] /= 100

    for percent in product([10, 20, 30, 40], repeat=len(emoticons)):
        prices = [0] * len(users)
        for i in range(len(percent)):
            for j in range(len(users)):
                if percent[i] >= users[j][0]:
                    prices[j] += emoticons[i] * (100 - percent[i])
        regist = 0
        price = 0
        for i in range(len(users)):
            if prices[i] >= users[i][1]:
                regist += 1
            else:
                price += prices[i]

        if maxRegist < regist:
            maxRegist = regist
            maxPrice = price
        elif maxRegist == regist:
            if maxPrice < price:
                maxPrice = price
    return [maxRegist, maxPrice]