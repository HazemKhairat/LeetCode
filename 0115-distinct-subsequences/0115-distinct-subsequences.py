class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def solve(idx1, idx2):
            if idx2 == len(t):
                return 1
            if idx1 == len(s):
                return 0

            take = skip = 0
            if s[idx1] == t[idx2]:
                take = solve(idx1 + 1, idx2 + 1)

            skip = solve(idx1 + 1, idx2)

            return take + skip

        return solve(0, 0)
