class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, ch in enumerate(s):
            res += (97 - ord(ch) + 26) * (i + 1)
        return res