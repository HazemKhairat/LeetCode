class Solution:
    def numSteps(self, s: str) -> int:
        s = s[::-1]
        num = 0
        for i in range(len(s)):
            num += int(s[i]) * (2**i)

        ans = 0
        while num > 1:
            ans += 1
            if num % 2 == 0:
                num //= 2
            else:
                num += 1

        return ans
