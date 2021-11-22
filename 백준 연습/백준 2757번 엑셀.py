import sys
mult = [0 for i in range(7)]
while True:
    R, C = map(int, sys.stdin.readline()[1:].split("C"))
    if R == 0 and C == 0:
        break
    div = 6
    while div > 0:
        mult[div] = C//pow(26, div)
        C -= (C//pow(26, div))*pow(26, div)
        div -= 1
    mult[0] = C
    for i in range(5):
        if mult[i] == 0 and mult[i+1] > 0:
            mult[i] += 26
            mult[i+1] -= 1
    for i in range(6,0,-1):
        if mult[i-1] == 0 and mult[i] > 0:
            mult[i-1] += 26
            mult[i] -= 1
    for i in range(6, -1, -1):
        if mult[i] != 0:
            print(chr(mult[i]+64), end="")
    print(R)

