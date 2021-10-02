import sys
n = int(sys.stdin.readline())
stack = []
input_num = []
output = []
num = 0
pop = 0
fail = False
for i in range(n):
    input_num.append(int(sys.stdin.readline()))
while pop < n:
    while num < input_num[pop]:
        num += 1
        stack.append(num)
        output.append("+")

    while num >= input_num[pop]:
        output.append("-")
        if stack.pop(-1) != input_num[pop]:
            fail = True
            break
        pop += 1
        if pop == n:
            break
    if fail:
        print("NO")
        break
if not fail:
    for i in range(len(output)):
        print(output[i])