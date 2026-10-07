class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = set()
        n = len(s)

        @cache
        def solve(r, o, c, idx, res):
            if idx == n:
                if o == c:
                    ans.add((r, res))
                return

            if s[idx] == "(":
                solve(r, o + 1, c, idx + 1, res + s[idx])
            elif s[idx] == ")" and c < o:
                solve(r, o, c + 1, idx + 1, res + s[idx])
            elif s[idx] not in ['(', ')']:
                solve(r, o, c, idx + 1, res + s[idx])

            solve(r + 1, o, c, idx + 1, res)


        solve(0, 0, 0, 0, "")
        ans = sorted(list(ans))
        res = [ans[0][1]]

        for i in range(1, len(ans)):
            if ans[i][0] == ans[i - 1][0]:
                res.append(ans[i][1]) 
            else:
                break
    
        return res
