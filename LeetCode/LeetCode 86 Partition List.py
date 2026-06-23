from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        under_x = deque()
        equal_over_x = deque()

        def dfs(node):
            if not node:
                return
            if node.val < x:
                under_x.append(node.val)
            else:
                equal_over_x.append(node.val)
            dfs(node.next)
        
        dfs(head)

        def dfs(node):
            if under_x:
                node.val = under_x.popleft()
            elif equal_over_x:
                node.val = equal_over_x.popleft()
            
            if under_x or equal_over_x:
                node.next = ListNode()
                dfs(node.next)
        
        answer = ListNode()

        dfs(answer)

        return answer