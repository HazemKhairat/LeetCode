class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = set(s)
        ans = 0
        for char in chars:
            i, j = s.index(char), s.rindex(char)
            st = set()
            for k in range(i + 1, j):
                st.add(s[k])
            ans += len(st)
        return ans
