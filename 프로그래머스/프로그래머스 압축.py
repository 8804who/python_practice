def solution(msg):
    answer = []

    lenMsg = len(msg)
    idx = 0
    dic = {}
    dicIdx = 27

    for i in range(26):
        dic[chr(i + 65)] = i + 1

    while idx < lenMsg:
        for i in range(lenMsg, idx, -1):
            if msg[idx:i] in dic:
                answer.append(dic[msg[idx:i]])
                if i < lenMsg:
                    dic[msg[idx:i + 1]] = dicIdx
                    dicIdx += 1
                idx = i
                break
    return answer