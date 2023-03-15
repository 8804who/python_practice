import sys


def find(A):
    if biggerCard[A] > A:
        return biggerCard[A]
    else:
        biggerCard[A] = find(biggerCard[A])
        return biggerCard[A]


N, K, M = map(int, sys.stdin.readline().split())

biggerCard = [0 for i in range(N+1)]
nums = list(map(int, sys.stdin.readline().split()))

first = 0
for num in nums:
    end = num
    for i in range(first, end):
        biggerCard[i] = num
    first = num

csCard = list(map(int, sys.stdin.readline().split()))
for card in csCard:
    print(biggerCard)
    print(find(card))

