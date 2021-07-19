sugar = int(input())
count = 0
while sugar != 0:
    if sugar % 5 == 0:
        count += sugar/5
        sugar = 0
    if sugar >= 5 and sugar % 3 != 0:
        count += 1
        sugar -= 5
    if sugar >= 3:
        count += 1
        sugar -= 3
    if sugar == 1 or sugar == 2:
        count = -1
        break
print(int(count))
