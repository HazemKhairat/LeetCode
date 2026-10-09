class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        ans = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == "(":
                stack.append("(")
                i += 1
            else:
                if i < n - 1 and s[i + 1] == ")":
                    i += 2
                else:
                    i += 1
                    ans += 1

                if stack:
                    stack.pop()
                else:
                    ans += 1

        ans += len(stack) * 2
        return ans
