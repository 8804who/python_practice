def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


def getCombination(n, m):
    return factorial(n+m)/(factorial(n)*factorial(m))


N, M, K = map(int, input().split())

if getCombination(N, M) < K:
    print(-1)
else:
    answer = ''
    while K > 0:
        combination = getCombination(N-1, M)
        if combination < K:
            K -= combination
            answer += 'z'
            M -= 1
        else:
            answer += 'a'
            N -= 1
        if N == 0:
            answer += 'z' * M
            break
        if M == 0:
            answer += 'a' * N
            break
    print(answer)