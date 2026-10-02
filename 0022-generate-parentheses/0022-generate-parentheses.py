class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        ans = []

        def isValid(s):
            stack = []

            for ch in s:
                if ch == "(":
                    stack.append(ch)
                elif stack:
                    stack.pop()

            return not stack

        def solve(s, o, c):
            nonlocal ans
            if o + c == n * 2 and isValid(s):
                ans.append(s)
                return

            if o < n:
                solve(s + "(", o + 1, c)
            if c < n:
                solve(s + ")", o, c + 1)

        solve("", 0, 0)
        return ans
