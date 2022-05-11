import re


def solution(str1, str2):
    intersectionNum = 0
    set1 = getTrimmedString(str1)
    set2 = getTrimmedString(str2)

    universalSetNum = len(set1) + len(set2)

    for i in range(len(set1)):
        for j in range(len(set2)):
            if set1[i] == set2[j]:
                intersectionNum += 1
                del set2[j]
                break

    if universalSetNum == 0:
        answer = 1
    else:
        answer = intersectionNum / (universalSetNum - intersectionNum)
    answer *= 65536

    return int(answer)


def getTrimmedString(string):
    s = []
    for i in range(len(string) - 1):
        text = re.sub('[^a-zA-Z]', ' ', string[i:i + 2]).strip()
        if len(text) == 2:
            s.append(text.upper())
    return s