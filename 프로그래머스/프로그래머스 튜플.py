def solution(s):
    answer = []
    dic = {}
    s = s.split('}')

    for i in s:
        i = i.split(',')
        for j in i:
            j = j.replace('{', '')
            if j == '':
                continue
            if j not in dic:
                dic[j] = 0
            if j in dic:
                dic[j] += 1
    arr = []
    for i in dic:
        arr.append([dic[i], i])
    arr.sort(reverse=True)
    for i in arr:
        answer.append(int(i[1]))
    return answer