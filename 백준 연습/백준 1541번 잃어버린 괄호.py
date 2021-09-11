exp = input()
e = exp.split('-')
Sum = 0
if len(e) == 1:
    One = exp.split('+')
    for i in range(len(One)):
        Sum += int(One[i])
    print(Sum)
else:
    for i in range(len(e)):
        count = 0
        ePart = e[i].split('+')
        for j in range(len(ePart)):
            count += int(ePart[j])
            if i != 0:
                Sum -= int(ePart[j])
            else:
                Sum += int(ePart[j])
    print(Sum)
    ''' 아래 코드는 괄호를 하나만 칠수 있을때의 최소값을 구하는 코드
    big = 0 
    for i in range(len(e)):
        count = 0
        ePart = e[i].split('+')
        for j in range(len(ePart)):
            count += int(ePart[j])
            if i != 0 and j == 0:
                Sum -= int(ePart[j])
            else:
                Sum += int(ePart[j])
        if big < count and i != 0:
            big = count-int(ePart[0])
    print(Sum-big*2)'''
