import sys
N = int(sys.stdin.readline())
prime_number = []
div = 2
while div <= N:
    if N % div == 0:
        prime_number.append(div)
    div += 1
prime_factor = []
i = 0
while N > 1:
    if N % prime_number[i] == 0:
        N /= prime_number[i]
        prime_factor.append(prime_number[i])
        i = 0
    else:
        i += 1
for i in range(len(prime_factor)):
    print(prime_factor[i])