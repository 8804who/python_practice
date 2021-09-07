n = int(input())
div = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        div.append(i)
        if i != int(n/i):
            div.append(int(n/i))
div.sort()
print(div)
