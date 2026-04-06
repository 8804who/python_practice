import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    string = list(input().rstrip())

    if string[0] == 'u':
        string[0] = 's'
        answer = 1
    else:
        answer = 0

    for i in range(1, len(string)-1):
        if string[i-1] == 's' and string[i] == 'u' and string[i+1] == 'u':
            string[i+1] = 's'
            answer += 1
    if string[-1] == 'u':
        answer += 1
        
    print(answer)
    