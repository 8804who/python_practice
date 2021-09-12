N = int(input())
Distance = list(map(int, input().split()))
OilPrice = list(map(int, input().split()))
Price, CityNumber = 0, 0
for i in range(len(OilPrice)):
    if i != CityNumber:
        continue
    GoDistance = 0
    for j in range(i, len(Distance)):
        GoDistance += Distance[j]
        CityNumber += 1
        if OilPrice[i] > OilPrice[j+1]:
            break
    Price += GoDistance * OilPrice[i]
print(Price)