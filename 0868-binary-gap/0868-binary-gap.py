class Solution:
    def binaryGap(self, n: int) -> int:
        prev, curr = -1, -1
        ans = 0

        while n:
            if n % 2 == 1 and prev == -1:
                prev = curr = 0
            elif n % 2 == 1:
                ans = max(ans, curr - prev)
                prev = curr

            if curr != -1:
                curr += 1
            n //= 2

        return ans
