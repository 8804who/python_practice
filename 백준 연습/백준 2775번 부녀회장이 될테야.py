import sys
T = int(sys.stdin.readline())
k = []
n = []
for i in range(T):
    k.append(int(sys.stdin.readline()))
    n.append(int(sys.stdin.readline()))
head = [[i for i in range(max(n)+1)]]
for i in range(1, max(k)+1):
    head.append([])
    for j in range(max(n)+1):
        num = 0
        for l in range(j+1):
            num += head[i - 1][l]
        head[i].append(num)
for i in range(T):
    print(head[k[i]][n[i]])
