class Solution:
    def maxProfit(self, p: List[int], s: List[int], k: int) -> int:
        n = len(p)
        orig = sum(p[i] * s[i] for i in range(n))

        pref_p = [0] * (n + 1)
        pref_s = [0] * (n + 1)

        for i in range(n):
            pref_p[i + 1] = pref_p[i] + p[i]
            pref_s[i + 1] = pref_s[i] + (p[i] * s[i])
        
        tmp = orig
        for l in range(n - k + 1):
            old = pref_s[l + k] - pref_s[l]
            new = pref_p[l + k] - pref_p[l + k // 2]
            orig = max(orig, tmp + (new - old))
        
        return orig