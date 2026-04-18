class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        ans = ""
        for i in range(len(s)):
            ch  = s[i]
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != ch:
                    return ans 
            ans += ch
        
        return ans

