import sys
N, K = map(int, sys.stdin.readline().split())
middle_idx = (K+1)//2

tree = [0] * (65536*4)


def Query(s, e, n, target):
    if s == e:
        return s

    m = (s+e)//2
    if tree[n*2] >= target:
        return Query(s, m, n*2, target)
    else:
        return Query(m+1, e, n*2+1, target-tree[n*2])


def Change(s, e, idx, num, n):
    if idx < s or idx > e:
        return 0
    tree[n] += num
    if s != e:
        m = (s+e)//2
        Change(s, m, idx, num, n*2)
        Change(m+1, e, idx, num, n*2+1)


arr = []
answer = 0

for _ in range(N):
    temperature = int(sys.stdin.readline())
    arr.append(temperature)
    Change(0, 65535, temperature, 1, 1)
    if len(arr) == K:
        answer += Query(0, 65535, 1, middle_idx)
        temperature = arr.pop(0)
        Change(0, 65535, temperature, -1, 1)
print(answer)