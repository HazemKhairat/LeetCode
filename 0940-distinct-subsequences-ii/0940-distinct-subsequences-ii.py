class Solution:
    def distinctSubseqII(self, s: str) -> int:
        total = 0
        dp = [0] * 26
        MOD = 10**9 + 7
        
        for ch in s:
            c = ord(ch) - 97
            new = 1 + total - dp[c]
            dp[c] = (dp[c] + new) % MOD
            total = (total + new) % MOD

        return total
