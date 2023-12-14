from collections import defaultdict


def dfs(port, graph, num_tickets, path):
    if num_tickets == 0:
        return path
    for next_port in graph[port]:
        if not next_port[1]:
            next_port[1] = True
            result = dfs(next_port[0], graph, num_tickets - 1, path + [next_port[0]])
            if result:
                return result
            next_port[1] = False


def solution(tickets):
    graph = defaultdict(list)
    for ticket in sorted(tickets):
        graph[ticket[0]].append([ticket[1], False])
    return dfs('ICN', graph, len(tickets), ['ICN'])