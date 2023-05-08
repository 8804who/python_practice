import sys


def union(A, B):
    a = find(A)
    b = find(B)

    if a <= b:
        friends[b] = a
    else:
        friends[a] = b


def find(A):
    if friends[A] == A:
        return A
    else:
        friends[A] = find(friends[A])
        return friends[A]


def enemys_enemy_is_friend(a, b):
    for enemy in enemys[b]:
        union(a, enemy)
    enemys[a].append(b)


input = sys.stdin.readline
n = int(input())

enemys = [[] for _ in range(n+1)]
friends = [i for i in range(n+1)]

for i in range(int(input())):
    r, p, q = input().split()
    p, q = int(p), int(q)
    if r == 'F':
        union(p, q)
    else:
        enemys_enemy_is_friend(p, q)
        enemys_enemy_is_friend(q, p)

print(len(set([find(i) for i in range(1, n+1)])))