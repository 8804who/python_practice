import sys
from collections import deque
expression = sys.stdin.readline().strip()
stack = deque()
for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(expression[i])
    elif expression[i] == ")":
        while stack:
            char = stack.pop()
            if char == "(":
                break
            else:
                print(char, end="")
    elif expression[i] == "+" or expression[i] == "-":
        while stack:
            char = stack.pop()
            if char == "(":
                stack.append("(")
                break
            else:
                print(char, end="")
        stack.append(expression[i])
    elif expression[i] == "*" or expression[i] == "/":
        if stack:
            if stack[-1] == "*" or stack[-1] == "/":
                print(stack.pop(), end="")
        stack.append(expression[i])
    else:
        print(expression[i], end="")
while stack:
    print(stack.pop(), end="")