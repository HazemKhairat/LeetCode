class Solution:
    def minOperations(self, s: str) -> int:
        start_with_1 = 0
        start_with_0 = 0

        for i in range(len(s)):
            start_with_1 += (i % 2 == 0 and s[i] == "0") + (i % 2 == 1 and s[i] == "1")
            start_with_0 += (i % 2 == 1 and s[i] == "0") + (i % 2 == 0 and s[i] == "1")

        return min(start_with_1, start_with_0)
