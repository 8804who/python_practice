import bisect
N = int(input())
wires = list(map(int, input().rstrip().split()))

lcs = [wires[0]]

for wire in wires[1:]:
    if lcs[-1] < wire:
        lcs.append(wire)
    else:
        lcs[bisect.bisect_left(lcs, wire)] = wire
print(N-len(lcs))