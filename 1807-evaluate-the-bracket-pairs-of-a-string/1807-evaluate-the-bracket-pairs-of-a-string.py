class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dic = {}
        for arr in knowledge:
            dic[arr[0]] = arr[1]
        # print(dic)

        n = len(s)
        ans = ""
        i = 0
        while i < n:
            if s[i] == "(":
                i += 1
                key = ""
                while i < n and s[i] != ")":
                    key += s[i]
                    i += 1
                if key in dic:
                    ans += dic[key]
                else:
                    ans += "?"
            else:
                ans += s[i]
            i += 1

        return ans
