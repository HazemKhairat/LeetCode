class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = []
        tmp = ""
        for ch in s:
            if ch == '(':
                stack.append(ch)
                tmp += ch
            elif stack:
                stack.pop()
                tmp += ch
            
            if not stack:
                res.append(tmp)
                tmp = ""
        
        ans = ""
        for st in res:
            n = len(st)
            ans += st[1:n - 1]

        return ans


