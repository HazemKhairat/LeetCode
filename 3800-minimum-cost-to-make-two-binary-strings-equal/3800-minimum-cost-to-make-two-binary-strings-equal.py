class Solution:
    def minimumCost(self, s: str, t: str, fc: int, sc: int, cc: int) -> int:
        if s == t:
            return 0
        n = len(s)
        c0 = c1 = 0
        for i in range(n):
            if s[i] != t[i] and s[i] == "0":
                c0 += 1
            elif s[i] != t[i] and s[i] == "1":
                c1 += 1
        diff = abs(c1 - c0)

        res1 = (c0 + c1) * fc

        res2 = (min(c0, c1) * sc) + (diff * fc)

        res3 = (min(c0, c1) * sc) + ((diff // 2) * (cc + sc)) + ((diff % 2) * fc)

        return min(res1, res2, res3)
