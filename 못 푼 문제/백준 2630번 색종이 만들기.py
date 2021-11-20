import sys
sys.setrecursionlimit(1000000000)


def cutpaper(paperMap, heiStart, heiEnd, widStart, widEnd):  # 종이와 탐색할 구간(세로시작점, 세로종료점, 가로시작점, 가로종료점)
    print(heiStart, heiEnd, widStart, widEnd)
    if heiStart == heiEnd and widStart == widEnd:
        if paperMap[int(heiStart)-1][int(widEnd)-1] == 1:
            print("1")
            return 1
        else:
            print("0")
            return 0
    elif heiStart > heiEnd or widStart > widEnd:
        return 0
    else:
        p1 = cutpaper(paperMap, heiStart, int(heiEnd/2), widStart, int(widEnd/2))
        p2 = cutpaper(paperMap, heiStart, int(heiEnd/2), int(widEnd/2)+widStart, widEnd)
        p3 = cutpaper(paperMap, int(heiEnd/2)+heiStart, heiEnd, widStart, int(widEnd/2))
        p4 = cutpaper(paperMap, int(heiEnd/2)+heiStart, heiEnd, int(widEnd/2)+widStart, widEnd)
        return p1+p2+p3+p4


N = int(sys.stdin.readline())
paper = []
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split(" "))))
print(cutpaper(paper, 1, 8, 1, 8))
