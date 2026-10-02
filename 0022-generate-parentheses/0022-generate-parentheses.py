class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def solve(s, o, c):
            nonlocal ans
            if o + c == n * 2:
                ans.append(s)
                return

            if o < n:
                solve(s + "(", o + 1, c)
            if c < o:
                solve(s + ")", o, c + 1)

        solve("", 0, 0)
        return ans
