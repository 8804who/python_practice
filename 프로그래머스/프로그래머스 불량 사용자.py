def check(banned_id, user):
    if len(banned_id) != len(user):
        return False

    for i in range(len(banned_id)):
        if banned_id[i] != '*' and banned_id[i] != user[i]:
            return False
    return True


def dfs(idx, banned_list, suspect_list):
    global case
    for banned_id in suspect_list[idx]:
        if banned_id not in banned_list:
            if idx == 0:
                case.add(str(sorted(banned_list + [banned_id])))
            else:
                dfs(idx - 1, banned_list + [banned_id], suspect_list)
    return len(case)


def solution(user_id, banned_id):
    global case
    case = set()
    suspect_list = [[] for _ in range(len(banned_id))]

    for i in range(len(banned_id)):
        for user in user_id:
            if check(banned_id[i], user):
                suspect_list[i].append(user)

    return dfs(len(banned_id) - 1, [], suspect_list)