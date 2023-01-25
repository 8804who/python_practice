def solution(n, left, right):
    answer=[]
    left+=1
    right+=1
    num=left
    while num<=right:
        if num%n==0:
            answer.append(n)
        else:
            answer.append(max(num//n+1,num%n))
        num+=1
    return answer