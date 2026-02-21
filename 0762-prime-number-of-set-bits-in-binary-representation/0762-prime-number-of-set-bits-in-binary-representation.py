from math import sqrt

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def countOnes(num):
            res = 0
            while num:
                res += num % 2 == 1
                num //= 2
            return res

        def isPrime(cnt):
            if cnt < 2:
                return False
            for i in range(2, int(math.sqrt(cnt)) + 1):
                if cnt % i == 0:
                    return False
            return True

        ans = 0
        for num in range(left, right + 1):
            cnt = countOnes(num)
            if isPrime(cnt):
                ans += 1

        return ans
