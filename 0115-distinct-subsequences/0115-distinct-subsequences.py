class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        @cache
        def backtrack(idxS, idxT):
            if idxT == m: return 1
            if idxS == n: return 0
            
            take = skip = 0
            if s[idxS] == t[idxT]:
                take += backtrack(idxS + 1, idxT + 1)
            
            skip += backtrack(idxS + 1, idxT)

            return take + skip

        return backtrack(0, 0)