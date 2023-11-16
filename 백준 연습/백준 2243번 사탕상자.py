import sys
N = int(sys.stdin.readline())

candys = [0] * 1000001
tree = [0] * 4000001


def Query(s, e, left, right, n):
    if e < left or s > right:
        return 0
    if left <= s and right >= e:
        return tree[n]
    m = (s+e)//2
    left_sum = Query(s, m, left, right, n*2)
    right_sum = Query(m+1, e, left, right, n*2+1)
    return left_sum+right_sum


def Change(s, e, idx, num, n):
    if idx < s or idx > e:
        return 0
    tree[n] += num
    if s != e:
        m = (s+e)//2
        Change(s, m, idx, num, n*2)
        Change(m+1, e, idx, num, n*2+1)


for command in range(N):
    input_values = list(map(int, sys.stdin.readline().split()))
    if input_values[0] == 1:
        start = 1
        end = 1000000
        answer = -1
        while start <= end:
            mid = (start+end)//2
            spot = Query(0, 1000000, 0, mid-1, 1)
            if spot >= input_values[1]:
                answer = mid
                end = mid-1
            else:
                start = mid+1
        print(answer)
        Change(0, 1000000, answer-1, -1, 1)
    else:
        Change(0, 1000000, input_values[1]-1, input_values[2], 1)