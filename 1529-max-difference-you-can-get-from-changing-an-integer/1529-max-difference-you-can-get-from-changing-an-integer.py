class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        t = s
        pos = 0
        while pos < len(s) and s[pos] == "9":
            pos += 1
        if pos < len(s):
            s = s.replace(s[pos], "9")

        pos = 0
        while pos < len(t) and t[pos] <= "1":
            pos += 1

        if pos == 0:
            t = t.replace(t[0], "1")
        elif pos < len(t):
            t = t.replace(t[pos], "0")

        return int(s) - int(t)
