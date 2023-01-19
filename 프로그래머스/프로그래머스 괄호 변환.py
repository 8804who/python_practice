def solution(p):
    return change(p)


def change(w):
    if len(w) == 0:
        return ''
    count = 0
    u = ''
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            u += w[0:i + 1]
            break
    v = w[len(u):]
    correct = True

    for i in u:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count == -1:
            correct = False
            break

    if correct:
        return u + change(v)
    else:
        temp = ''
        for c in u:
            if c == '(':
                temp += ')'
            else:
                temp += '('
        return '(' + change(v) + ')' + temp[1:-1]