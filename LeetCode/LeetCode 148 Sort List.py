# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        def dfs(node):
            if not node:
                return
            nums.append(node.val)
            dfs(node.next)

        dfs(head)
        nums.sort()

        def dfs(node):
            if not node:
                return
            node.val = nums.pop(0)
            dfs(node.next)
        dfs(head)
        return head