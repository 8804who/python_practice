import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
sorted_B = sorted(B)
size = [-1 for i in range(len(B))]
Sum = 0
for i in range(len(B)):
    for j in range(len(B)):
        if B[i] == sorted_B[j]:
            while True:
                if j in size:
                    j += 1
                else:
                    size[i] = j
                    break
            break
A.sort(reverse=True)
for i, j in zip(range(len(A)), size):
    Sum += A[j]*B[i]
print(Sum)
