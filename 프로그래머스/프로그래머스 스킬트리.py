def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_idx = 0
        can = True

        for s in skill_tree:
            if skill_idx == len(skill):
                break
            if s == skill[skill_idx]:
                skill_idx += 1
                continue
            for i in range(skill_idx + 1, len(skill)):
                if s == skill[i]:
                    can = False
        if can:
            answer += 1
    return answer