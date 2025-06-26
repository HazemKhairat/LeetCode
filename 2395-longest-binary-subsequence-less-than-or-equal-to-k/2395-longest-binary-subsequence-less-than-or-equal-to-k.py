class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        res_str = ""
        for i in range(n - 1, -1, -1):
            tmp = res_str
            if s[i] == "1":
                if int(s[i] + tmp, 2) <= k:
                    res_str = s[i] + tmp
            else:
                res_str = s[i] + tmp

        return len(res_str)
