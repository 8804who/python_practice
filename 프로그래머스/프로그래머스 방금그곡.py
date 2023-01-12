def solution(m, musicinfos):
    answer = '(None)'
    info = []
    maxTime = 0
    music = []

    for i in range(len(m)):
        if m[i] == "#":
            music[-1] += "#"
        else:
            music.append(m[i])

    for i in musicinfos:
        info.append(i.split(','))

    for i in info:
        start = i[0].split(':')
        end = i[1].split(':')
        time = 0
        song = []

        for j in range(len(i[3])):
            if i[3][j] == "#":
                song[-1] += "#"
            else:
                song.append(i[3][j])

        songLength = len(song)
        time += (int(end[0]) - int(start[0])) * 60
        time += (int(end[1]) - int(start[1]))
        songPlay = song * (time // songLength) + song[0:time % songLength]

        count = 0
        for j in songPlay:
            if j == music[count]:
                count += 1
            else:
                count = 0
                if j == music[count]:
                    count += 1
            if count == len(music):
                if time > maxTime:
                    answer = i[2]
                    maxTime = time
                break
    return answer