class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for ch in s:
            if ch not in ['*', '#', '%']:
                res.append(ch)
            elif res and ch == '*':
                res.pop()
            elif ch == '#':
                res = res + res
            elif ch == '%':
                res.reverse()
        
        return "".join(res)
                