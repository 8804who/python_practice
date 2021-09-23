import sys


def stack_pop(stack):
    n = stack[-1]
    del stack[-1]
    return n


def stack_push(stack, n):
    stack.append(n)


num_stack = []
for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        stack_pop(num_stack)
    else:
        stack_push(num_stack, num)
print(sum(num_stack))
