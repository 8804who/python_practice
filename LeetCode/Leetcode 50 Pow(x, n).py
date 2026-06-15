class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        def divide_pow(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n % 2 == 0:
                return divide_pow(x, n/2) ** 2
            else:
                return divide_pow(x, (n-1)/2) ** 2 * x
        return divide_pow(x,n)