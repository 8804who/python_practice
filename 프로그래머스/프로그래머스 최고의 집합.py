def solution(n, s):
    answer = []
    if n>s:
        answer.append(-1)
        n=0
    while n>0:
        answer.append(s//n)
        s-=s//n
        n-=1
    return answer