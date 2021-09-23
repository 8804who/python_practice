import sys
import math

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()
    for l1 in range(n):
        for l2 in range(n):
            for r1 in range(math.floor(n/2)+l1-1, n):
                for r2 in range(math.floor(n/2)+l2-1, n):
                    if l1 != l2 or r1 != r2:
                        if int(s[l2:r2+1], 2) == 0:
                            print(l1+1, r1+1, l2+1, r2+1)
                            ans = True
                            break
                        elif int(s[l1:r1+1], 2) % int(s[l2:r2+1], 2) == 0:
                            print(l1+1, r1+1, l2+1, r2+1)
                            ans = True
                            break
                if ans:
                    break
            if ans:
                break
        if ans:
            break

