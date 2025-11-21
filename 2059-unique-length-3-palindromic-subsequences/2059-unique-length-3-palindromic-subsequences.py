class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        s = list(s)
        start = Counter()
        for i, ch in enumerate(s):
            if ch not in start:
                start[ch] = i

        end = Counter()
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch not in end:
                end[ch] = i

        ans = 0
        for i in range(97, 123):
            ch = chr(i)
            f, e = start[ch], end[ch]
            st = set()
            for j in range(f + 1, e):
                st.add(s[j])
            ans += len(st)
        return ans
