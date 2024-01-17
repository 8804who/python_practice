import sys

sys.setrecursionlimit(200000)


def union(A, parent):
    parent[A] = find(A + 1, parent)


def find(A, parent):
    if A not in parent:
        parent[A] = A
    if parent[A] != A:
        parent[A] = find(parent[A], parent)
        return parent[A]
    else:
        return A


def solution(k, room_number):
    answer = []
    parent = {}

    for number in room_number:
        answer.append(find(number, parent))
        union(answer[-1], parent)
    return answer