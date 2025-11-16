class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        ans, consecutive = 0, 0
        for i in range(n):
            if s[i] == '0':
                ans += consecutive * (consecutive + 1) // 2
                consecutive = 0
            else:
                consecutive += 1
        ans += consecutive * (consecutive + 1) // 2
        return ans % MOD
