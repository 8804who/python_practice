def solution(s):
    answer = ''
    s = s.split(" ")

    minNum = int(s[0])
    maxNum = int(s[0])
    for n in s:
        if int(n) > maxNum:
            maxNum = int(n)
        if int(n) < minNum:
            minNum = int(n)
    return str(minNum) + " " + str(maxNum)