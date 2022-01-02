import sys


def searchPaper(paperArr, N):
    paperSum = 0
    for h in range(N):
        paperSum += sum(paperArr[h])
    if paperSum == N**2:
        return [1]
    elif paperSum == 0:
        return [0]
    else:
        cut1 = []
        cut2 = []
        cut3 = []
        cut4 = []
        for h in range(0, N//2):
            cut1.append(paperArr[h][0:N//2])
            cut3.append(paperArr[h][N//2:N])
        for h in range(N//2, N):
            cut2.append(paperArr[h][0:N//2])
            cut4.append(paperArr[h][N//2:N])
        return searchPaper(cut1, N//2)+searchPaper(cut2, N//2)+searchPaper(cut3, N//2)+searchPaper(cut4, N//2)


N = int(sys.stdin.readline())
paper = []
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

blue = 0
white = 0
result = searchPaper(paper, N)
for i in range(len(result)):
    if result[i] == 1:
        blue += 1
    else:
        white += 1
print(white)
print(blue)

