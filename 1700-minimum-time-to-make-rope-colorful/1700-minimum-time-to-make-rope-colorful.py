class Solution:
    def minCost(self, colors: str, nt: List[int]) -> int:
        c = list(colors)
        ans = 0
        for i in range(1, len(c)):
            if c[i] == c[i - 1]:
                if nt[i] < nt[i - 1]:
                    ans += nt[i]
                    c[i], nt[i] = "*", -1
                    c[i], c[i - 1] = c[i - 1], c[i]
                    nt[i], nt[i - 1] = nt[i - 1], nt[i]
                else:
                    ans += nt[i - 1]
                    c[i - 1], nt[i - 1] = "*", -1
        return ans
