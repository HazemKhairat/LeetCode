class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                stack.pop()
            ans = max(ans, len(stack))
        
        return ans