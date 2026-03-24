import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    binary = input().rstrip()

    length = len(binary)
    zero_count = binary.count('0')
    one_count = length - zero_count

    if zero_count % 2 == 1:
        print(zero_count)
        for i in range(length):
            if binary[i] == '0':
                print(i+1, end=' ')
        print()
    elif one_count % 2 == 0:
        print(one_count)
        if one_count != 0:
            for i in range(len(binary)):
                if binary[i] == '1':
                    print(i+1, end = ' ')
            print()
    else:
        print(-1)