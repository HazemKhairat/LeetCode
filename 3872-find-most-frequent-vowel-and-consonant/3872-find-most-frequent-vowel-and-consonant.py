class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = Counter()
        c = Counter()

        for ch in s:
            if ch in "aeiou":
                v[ch] += 1
            else:
                c[ch] += 1
        print(c)
        print(v)
        a = (max(v.values()) if v else 0)
        b = (max(c.values()) if c else 0)
        return a + b