import math
def solution(n, k):
    answer = []
    factorial=[0,1,2]
    arr=[i for i in range(0,n+1)]
    for i in range(n-2):
        factorial.append((i+3)*factorial[i+2])
    n-=1
    while n>0:
        i=math.ceil(k/factorial[n])
        k%=factorial[n]
        if i==0:
            i=-1
        answer.append(arr[i])
        del arr[i]
        n-=1
    answer.append(arr[-1])
    return answer