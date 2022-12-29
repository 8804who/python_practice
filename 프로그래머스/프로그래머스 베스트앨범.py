import operator


def solution(genres, plays):
    answer = []
    totalPlay = dict()
    genre1st = dict()
    genre2nd = dict()

    for genre, play, i in zip(genres, plays, range(len(genres))):
        if genre in totalPlay:
            totalPlay[genre] += play
        else:
            totalPlay[genre] = play

        if genre not in genre1st:
            genre1st[genre] = [play, i]
        else:
            if genre1st[genre][0] < play:
                genre2nd[genre], genre1st[genre] = genre1st[genre], [play, i]
            else:
                if genre not in genre2nd:
                    genre2nd[genre] = [play, i]
                else:
                    if genre2nd[genre][0] < play:
                        genre2nd[genre] = [play, i]

    for i in sorted(totalPlay.items(), key=operator.itemgetter(1), reverse=True):
        answer.append(genre1st[i[0]][1])
        if i[0] in genre2nd:
            answer.append(genre2nd[i[0]][1])
    return answer