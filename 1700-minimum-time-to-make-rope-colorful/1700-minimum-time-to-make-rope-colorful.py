class Solution:
    def minCost(self, colors: str, nt: List[int]) -> int:
        c = list(colors)
        ans = 0
        for i in range(1, len(c)):
            if c[i] == c[i - 1]:
                ans += min(nt[i], nt[i - 1])
                nt[i] = max(nt[i], nt[i - 1])
        return ans
