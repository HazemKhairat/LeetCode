class Solution:
    def myPow(self, x: float, n: int) -> float:

        def calc_power(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = self.myPow(x, n // 2)
            res = res * res

            if n % 2 == 1:
                return res * x

            return res

        ans = calc_power(x, abs(n))

        return ans if n >= 0 else (1 / ans)
