import sys
import bisect
input = sys.stdin.readline
T = int(input())

for test_case in range(T):
    k, n = map(int, input().split())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    AB=[]
    CD=[]
    
    for a in A:
        for b in B:
            AB.append(a+b)
    for c in C:
        for d in D:
            CD.append(c+d)

    AB.sort()
    CD.sort()

    answer = 1e9
    for ab in AB:
        find = k-ab

        num1 = bisect.bisect_left(CD, find)
        num2 = num1-1
        if num1==len(CD):
            num1 -= 1

        num1 = CD[num1]+ab
        num2 = CD[num2]+ab

        if abs(k-answer)>abs(k-num1):
            answer = num1
        elif abs(k-answer)==abs(k-num1):
            if answer > num1:
                answer = num1
        
        if abs(k-answer)>abs(k-num2):
            answer = num2
        elif abs(k-answer)==abs(k-num2):
            if answer > num2:
                answer = num2
    print(answer)