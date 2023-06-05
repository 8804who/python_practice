for i in range(int(input())):
    s=input().split('+')
    if len(s) == 2:
        print(int(s[0])+int(s[1]))
    else:
        print('skipped')