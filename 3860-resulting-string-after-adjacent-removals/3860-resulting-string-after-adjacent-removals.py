class Solution:
    def resultingString(self, s: str) -> str:
        stack = []

        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                first = ord(stack.pop())
                second = ord(ch)
                if abs(first - second) == 25:
                    continue
                elif abs(first - second) != 1:
                    stack.append(chr(first))
                    stack.append(ch)
                
        res = ""
        while stack:
            res += stack.pop()
        res = res[::-1]
            
        return res