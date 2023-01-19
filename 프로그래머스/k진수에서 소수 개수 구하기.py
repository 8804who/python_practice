def solution(n, k):
    answer = 0
    s = ''
    d = 0
    maxNum = 0
    while k ** d <= n:
        d += 1

    while d >= 0:
        s += str(n // (k ** d))
        n %= k ** d
        d -= 1
    s = s.split('0')

    for i in s:
        if i != '' and i != '1':
            prime = True
            for j in range(2, int(int(i) ** 0.5) + 1):
                if int(i) % j == 0:
                    prime = False
                    break
            if prime:
                answer += 1
    return answer