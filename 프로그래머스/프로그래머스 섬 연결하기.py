def solution(n, costs):
    answer = 0
    parent = [i for i in range(n + 1)]

    def find(x):
        if parent[x] != x:
            return find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    costs.sort(key=lambda x: x[2])

    for cost in costs:
        a = cost[0]
        b = cost[1]
        price = cost[2]

        if find(a) != find(b):
            answer += price
            union(a, b)
    return answer