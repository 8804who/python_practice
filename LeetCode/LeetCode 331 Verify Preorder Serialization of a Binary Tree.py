class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")

        if preorder == ["#"]:
            return True

        stack = []
        parent = -1
        for node in preorder:
            if node != "#":
                if parent == -1:
                    parent = 1
                else:
                    parent += 1
            stack.append(node)
            while len(stack) >= 3:
                if stack[-1] == "#" and stack[-2] == "#":
                    stack.pop()
                    stack.pop()
                    parent -= 1
                    stack[-1] = "#"
                else:
                    break

        return True if parent == 0 and stack == ["#"] else False