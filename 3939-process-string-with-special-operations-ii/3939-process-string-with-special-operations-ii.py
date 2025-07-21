class Solution:
    def processStr(self, s: str, k: int) -> str:
        l = 0

        for ch in s:
            if ch == '*':
                l = max(0, l - 1)
            elif ch == '#':
                l *= 2
            elif ch == '%':
                continue
            else:
                l += 1
            
        if k >= l:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == '*':
                l += 1
            elif ch == '#':
                l //= 2
                if k >= l:
                    k -= l
            elif ch == '%':
                k = l - 1 - k
            else:
                l -= 1
                if k == l:
                    return ch
        
        return '.'
        
