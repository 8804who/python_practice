import sys
T = int(sys.stdin.readline())
for Case in range(T):
    N = int(sys.stdin.readline())
    Applicant = []
    fail = 0
    for i in range(N):
        Applicant.append(list(map(int, sys.stdin.readline().split())))
    Applicant.sort()
    UppersTest2Min = Applicant[0][1]
    for i in range(1, N):
        if UppersTest2Min < Applicant[i][1]:
            fail += 1
        else:
            UppersTest2Min = Applicant[i][1]
    print(N-fail)
