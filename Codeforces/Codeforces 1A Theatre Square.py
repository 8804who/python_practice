import sys

input = sys.stdin.readline

n, m, a = map(int, input().split())

x = n//a + (0 if n%a == 0 else 1)
y = m//a + (0 if m%a == 0 else 1)

print(x*y)