class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even, odd = (n + 1) // 2, n // 2

        def fastExpon(a, b):
            res = 1
            while b > 0:
                if b % 2 == 1:
                    res = res * a % mod
                a = a * a % mod
                b //= 2
            return res

        return fastExpon(5, even) * fastExpon(4, odd) % mod
