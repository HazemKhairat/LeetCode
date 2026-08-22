class Solution:
    def checkDivisibility(self, n: int) -> bool:
        Sum, prod = 0, 1

        tmp = n
        while tmp:
            Sum += (tmp % 10)
            prod *= (tmp % 10)
            tmp //= 10
        return n % (Sum + prod) == 0