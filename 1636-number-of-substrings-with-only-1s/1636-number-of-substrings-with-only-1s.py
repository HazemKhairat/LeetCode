class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        i = j = 0
        ans = 0
        while j < len(s):
            while j < len(s) and s[j] == "0":
                j += 1
            i = j
            while j < len(s) and s[j] == "1":
                ans += (j - i + 1) % MOD
                j += 1
        return ans % MOD
