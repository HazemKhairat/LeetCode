class Solution:
    def lastInteger(self, n: int) -> int:
        start, step, rightToLeft = 1, 1, False

        while n > 1:
            if n % 2 == 0 and rightToLeft:
                start += step
            step *= 2
            n = (n + 1) // 2
            rightToLeft ^= True

        return start
