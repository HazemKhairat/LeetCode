class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = ""
        tmp = []
        ans = [s[i] if not s[i].isalpha() else "" for i in range(len(s))]
        
        for ch in s:
            if ch.isalpha():
                tmp.append(ch)
        
        
        i = 0
        for j in range(len(ans) - 1, -1, -1):
            if not ans[j]:
                ans[j] = tmp[i] 
                i += 1
                       
        res = ''.join(ans)
        return res