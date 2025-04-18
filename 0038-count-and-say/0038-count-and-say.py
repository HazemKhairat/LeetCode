class Solution:
    def countAndSay(self, n: int) -> str:

        def dfs(s, step):
            if step == n:
                return s

            newString = []

            i = 0
            while i < len(s):
                cnt = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    cnt += 1
                    i += 1
                newString.append(str(cnt))
                newString.append(s[i])
                i += 1
            return dfs("".join(newString), step + 1)

        return dfs("1", 1)

        # 0 1
        # 2 1
        # 1 -> 0
        # 2 -> 0

        # newString = 1211
