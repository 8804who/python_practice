import sys
for i in range(int(sys.stdin.readline())):
    stack = list(sys.stdin.readline())[:-1]
    length = len(stack)
    left, right = 0, 0
    for j in range(length):
        if stack.pop() == '(':
            left += 1
        else:
            right += 1
        if left > right:
            print("NO")
            break
        if j == length-1:
            if left == right:
                print("YES")
            else:
                print("NO")