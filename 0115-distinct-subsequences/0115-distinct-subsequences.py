class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        memo = [[-1] * n for _ in range(n)]

        def backtrack(idxS, idxT):
            if idxT == m: return 1
            if idxS == n: return 0

            if memo[idxS][idxT] != -1:
                return memo[idxS][idxT]
            
            take = skip = 0
            if s[idxS] == t[idxT]:
                take += backtrack(idxS + 1, idxT + 1)
            
            skip += backtrack(idxS + 1, idxT)
            memo[idxS][idxT] = take + skip
            return memo[idxS][idxT]

        return backtrack(0, 0)