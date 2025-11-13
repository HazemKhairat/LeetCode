class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        ans = 0
        left_ones = 0
        for i in range(n):
            if s[i] == "1":
                left_ones += 1
            elif s[i] == "0" and (i == n - 1 or s[i + 1] == "1"):
                ans += left_ones

        return ans
