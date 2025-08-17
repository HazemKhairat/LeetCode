class Solution:
    def maxProfit(self, p: List[int], s: List[int], k: int) -> int:
        n = len(p)

        original = sum(p[i] * s[i] for i in range(n))

        pref_s = [0] * (n + 1)
        pref_p = [0] * (n + 1)

        for i in range(n):
            pref_s[i + 1] = pref_s[i] + s[i] * p[i]
            pref_p[i + 1] = pref_p[i] + p[i]


        maxi = -inf

        for l in range(n - k + 1):
            prev = pref_s[l + k] - pref_s[l]
            curr = pref_p[l + k] - pref_p[l + ( k // 2)]
            maxi = max(maxi, curr - prev)

        return original + max(0, maxi)