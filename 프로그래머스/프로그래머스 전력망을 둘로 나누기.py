from collections import Counter


def solution(n, wires):
    answer = n
    wires.sort(key=lambda x: (x[0], x[1]))

    for i in range(n - 1):
        parents = [idx for idx in range(n + 1)]
        for j in range(n - 1):
            if i == j:
                continue
            else:
                union(wires[j][0], wires[j][1], parents)

        new = []
        for i in range(1, n + 1):
            new.append(find(i, parents))
        counter = Counter(new)
        counter = list(counter.values())
        answer = min(answer, abs(counter[0] - counter[1]))
    return answer


def find(a, parent):
    if a != parent[a]:
        parent[a] = find(parent[a], parent)
    return parent[a]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b