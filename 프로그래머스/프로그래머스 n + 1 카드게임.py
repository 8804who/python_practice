from collections import deque

def solution(coin, cards):
    answer = 0
    n = len(cards)
    q = deque()
    count = 0
    in_hand = set(cards[:n//3])
    for i in cards[:n//3]:
        if n+1-i in cards[:n//3]:
            count += 1
    count//=2

    cards = cards[(n//3):]
    temp = set()
    for i in range(0,len(cards),2):
        answer += 1
        temp.add(cards[i])
        temp.add(cards[i+1])
        count -= 1
        if count < 0:
            temp1 = -1
            temp2 = -1
            for j in in_hand:
                if n+1-j in temp and coin >= 1:
                    coin -= 1
                    count += 1
                    temp1 = j
                    temp2 = n+1-j
                    break
            in_hand-=set([temp1])
            temp-=set([temp2])
            if count >= 0:
                continue
            for j in temp:
                if n+1-j in temp and coin >= 2:
                    coin -= 2
                    count += 1
                    temp1 = j
                    temp2 = n+1-j
                    break
            temp-=set([temp1, temp2])

        if count < 0:
            break
    if count >= 0:
        answer += 1
    return answer