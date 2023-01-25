def solution(n):
    answer = 0
    num=1
    start=1
    end=2
    while end<=n:
        if num==n:
            answer+=1
            num+=end
            end+=1
        elif num>n:
            num-=start
            start+=1
        else:
            num+=end
            end+=1
    return answer+1