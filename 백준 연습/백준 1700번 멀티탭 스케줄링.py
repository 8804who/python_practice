import sys
input = sys.stdin.readline
N, K = map(int, input().split())

use = tuple(map(int, input().split()))
usingMachine = set()
usingSocket = 0
count = 0
for i, m in enumerate(use):
    if m in usingMachine:
        continue
    if usingSocket < N:
        usingMachine.add(m)
        usingSocket += 1
        continue
    else:
        temp = set() | usingMachine
        for j in range(i+1, K):
            if len(temp) > 1 and use[j] in temp:
                temp.remove(use[j])
        if len(temp) >= 1:
            usingMachine.remove(temp.pop())
            usingMachine.add(m)
            count += 1
print(count)