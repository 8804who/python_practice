def solution(n):
    count = 0
    for i in range(1, n+1):
        word = str(i)
        if len(word) > 2:
            diff = int(word[1]) - int(word[0])
            for j in range(len(word)-1):
                if int(word[j + 1]) - int(word[j]) != diff:
                    break
                if j == len(word) - 2:
                    count += 1
        else:
            count += 1
    print(count)


solution(int(input()))
