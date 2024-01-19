def solution(n, build_frame):
    answer = []
    pillar_frame = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    beam_frame = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    pillar_fixture = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    beam_fixture = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    for i in range(n + 1):
        pillar_fixture[0][i] = 1

    for build in build_frame:
        x, y, a, b = build
        if b == 0:
            if a == 0:
                if pillar_frame[y + 1][x] == 1 and pillar_fixture[y + 1][x] == 1:
                    continue
                if x - 1 >= 0 and beam_frame[y + 1][x - 1] == 1 and beam_fixture[y + 1][x - 1] < 4:
                    continue
                if beam_frame[y + 1][x] == 1 and beam_fixture[y + 1][x] < 4:
                    continue
                pillar_fixture[y + 1][x] -= 1
                beam_fixture[y + 1][x] -= 2
                if x - 1 >= 0:
                    beam_fixture[y + 1][x - 1] -= 2
                pillar_frame[y][x] = 0
            else:
                if x - 1 >= 0 and beam_frame[y][x - 1] == 1 and beam_fixture[y][x - 1] < 3:
                    continue
                if beam_frame[y][x + 1] == 1 and beam_fixture[y][x + 1] < 3:
                    continue
                if pillar_frame[y][x + 1] == 1 and pillar_fixture[y][x + 1] == 1:
                    continue
                if pillar_frame[y][x] == 1 and pillar_fixture[y][x] == 1:
                    continue
                if x - 1 >= 0:
                    beam_fixture[y][x - 1] -= 1
                beam_fixture[y][x + 1] -= 1
                pillar_fixture[y][x + 1] -= 1
                pillar_fixture[y][x] -= 1
                beam_frame[y][x] = 0
        else:
            if a == 0:
                if pillar_fixture[y][x] > 0:
                    pillar_frame[y][x] = 1
                    pillar_fixture[y + 1][x] += 1
                    if x - 1 >= 0:
                        beam_fixture[y + 1][x - 1] += 2
                    beam_fixture[y + 1][x] += 2
            else:
                if beam_fixture[y][x] > 1:
                    beam_frame[y][x] = 1
                    if x - 1 >= 0:
                        beam_fixture[y][x - 1] += 1
                    beam_fixture[y][x + 1] += 1
                    pillar_fixture[y][x + 1] += 1
                    pillar_fixture[y][x] += 1

    for x in range(n + 1):
        for y in range(n + 1):
            if pillar_frame[y][x] == 1:
                answer.append([x, y, 0])
            if beam_frame[y][x] == 1:
                answer.append([x, y, 1])
    return answer