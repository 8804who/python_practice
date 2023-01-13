def solution(expression):
    answer = 0
    nums = [0]
    oper = ['+', '-', '*']
    for i in expression:
        if i == '+' or i == '-' or i == '*':
            nums.append(i)
            nums.append(0)
        else:
            nums[-1] = int(str(nums[-1]) + str(i))

    for first in range(3):
        temp = []
        operland = False
        for i in nums:
            if i == oper[first]:
                operland = True
                continue
            elif operland:
                operland = False
                if oper[first] == '+':
                    temp[-1] += i
                elif oper[first] == '-':
                    temp[-1] -= i
                else:
                    temp[-1] *= i
                continue
            else:
                temp.append(i)

        for second in range(3):
            if first == second:
                continue
            temp2 = []
            operland = False
            for i in temp:
                if i == oper[second]:
                    operland = True
                    continue
                if operland:
                    operland = False
                    if oper[second] == '+':
                        temp2[-1] += i
                    elif oper[second] == '-':
                        temp2[-1] -= i
                    else:
                        temp2[-1] *= i
                    continue
                temp2.append(i)

            num = 0
            for i in temp2:
                if i in oper:
                    operland = True
                    continue
                if operland:
                    operland = False
                    operNum = 3 - first - second
                    if operNum == 0:
                        num += i
                    elif operNum == 1:
                        num -= i
                    else:
                        num *= i
                    continue
                num = i
            if num < 0:
                num = -num
            answer = max(answer, num)

    return answer