class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = str(-x)
        else:
            s = str(x)

        s = s[::-1]
        n = int(s) if x >= 0 else -int(s)
        if n > 2**31-1 or n < -(2**31):
            return 0
        return n