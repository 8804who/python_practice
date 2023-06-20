import sys
from bisect import bisect_right


def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


N, M, K = map(int, sys.stdin.readline().split())

parent = [i for i in range(M)]

cards = list(map(int, sys.stdin.readline().rstrip().split()))
cs_cards = list(map(int, sys.stdin.readline().rstrip().split()))

cards.sort()

for cs_card in cs_cards:
    num = bisect_right(cards, cs_card)
    print(cards[find(num)])
    if find(num)+1 < M:
        A = find(num)
        B = find(num)+1
        parent[A] = B
