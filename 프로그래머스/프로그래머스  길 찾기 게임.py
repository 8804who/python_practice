import sys

sys.setrecursionlimit(10000)


class tree_node:
    def __init__(self, x, idx, right_limit):
        self.x = x
        self.idx = idx
        self.right_limit = right_limit


def preorder(node, graph):
    pre = []
    q = [node]
    while q:
        node = q.pop()
        pre.append(node)
        for n in graph[node][::-1]:
            q.append(n)
    return pre


def postorder(node, graph, post):
    for n in graph[node]:
        postorder(n, graph, post)
    post.append(node)
    return post


def solution(nodeinfo):
    for idx, node in enumerate(nodeinfo):
        node.append(idx + 1)
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    graph = [[] for _ in range(len(nodeinfo) + 1)]
    level, head = nodeinfo[0][1], nodeinfo[0][2]

    parent = []
    brother = [tree_node(nodeinfo[0][0], nodeinfo[0][2], 100001)]
    nodeinfo.pop(0)

    for node in nodeinfo:
        if level > node[1]:
            parent = []
            while brother:
                parent.append(brother.pop(0))
            level = node[1]
        while parent:
            if parent[0].x > node[0]:  # 왼쪽 자녀 노드
                brother.append(tree_node(node[0], node[2], parent[0].x))
                graph[parent[0].idx].append(node[2])
                break
            elif node[0] < parent[0].right_limit:  # 오른쪽 자녀 노드
                brother.append(tree_node(node[0], node[2], parent[0].right_limit))
                graph[parent[0].idx].append(node[2])
                break
            else:
                parent.pop(0)  # 해당 노드의 자녀가 아님
    return [preorder(head, graph), postorder(head, graph, [])]