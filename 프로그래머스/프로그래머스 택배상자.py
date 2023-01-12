from collections import deque


def solution(order):
    answer = 0
    arr=[[i+1, order[i]] for i in range(len(order))]
    arr.sort(key = lambda x:x[1])
    stack=deque()
    count=1

    for i in range(len(order)):
        if arr[i][0]==count:
            count+=1
            answer+=1
            while stack:
                if stack[-1][0]==count:
                    stack.pop()
                    count+=1
                    answer+=1
                else:
                    break
        else:
            stack.append(arr[i])
    return answer