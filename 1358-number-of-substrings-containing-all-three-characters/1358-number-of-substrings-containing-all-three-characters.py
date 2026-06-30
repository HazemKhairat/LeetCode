class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        lastAppear = [-1] * 3
        ans = 0
        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            lastAppear[idx] = i
            if lastAppear[0] > -1 and lastAppear[1] > -1 and lastAppear[2] > -1:
                ans += 1 + min(lastAppear)

        return ans
