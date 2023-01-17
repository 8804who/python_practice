def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    totalGame=len(A)
    idx=0
    for s1 in A:
        while idx < totalGame:
            if B[idx]>s1:
                answer+=1
                idx+=1
                break
            else:
                idx+=1
    return answer