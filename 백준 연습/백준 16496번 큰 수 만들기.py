int(input())
arr = [s[1] for s in sorted([[s*10, s] for s in list(map(str, input().split()))], reverse=True, key=lambda x: x[0][:10])]
answer = ''
for s in arr:
    answer += s
print(int(answer))