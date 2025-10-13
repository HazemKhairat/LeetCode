class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)

        @cache
        def solve(tmp, idx):
            if idx == n:
                return tmp == ""

            ch = s[idx]
            newWord = False
            if (tmp + ch) in word_set:
                newWord = solve("", idx + 1)
            ok = solve(tmp + ch, idx + 1)

            return ok or newWord

        return solve("", 0)
