import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    students = [list(map(int, input().split())) for _ in range(M)]

    students.sort(key=lambda x:[x[1],-x[0]])

    books = [False] * (N+1)

    ans = 0

    for student in students:
        for i in range(student[0],student[1]+1):
            if not books[i]:
                books[i] = True
                ans += 1
                break

    print(ans)