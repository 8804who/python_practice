import sys
while True:
    st = sys.stdin.readline().replace('\n', '')
    if st == '.':
        break
    string = list(map(str, st))
    open = []
    isBalanced = True
    while string:
        word = string.pop()
        if word == ')' or word == ']':
            open.append(word)
        if word == '(':
            if len(open) == 0:
                isBalanced = False
                break
            if open.pop() == ']':
                isBalanced = False
                break
        if word == '[':
            if len(open) == 0:
                isBalanced = False
                break
            if open.pop() == ')':
                isBalanced = False
                break
    if len(string) == 0 and len(open) == 0 and isBalanced:
        print("yes")
    else:
        print("no")
