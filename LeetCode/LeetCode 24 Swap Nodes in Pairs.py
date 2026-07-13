# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = []
        def dfs(node):
            if not node:
                return
            q.append(node.val)
            dfs(node.next)
        
        dfs(head)
        

        for i in range(0, len(q),2):
            if i+1 < len(q):
                q[i], q[i+1] = q[i+1], q[i]
        
        def dfs(node):
            if not node:
                return
            node.val = q.pop(0)
            dfs(node.next)
        
        dfs(head)
        return head