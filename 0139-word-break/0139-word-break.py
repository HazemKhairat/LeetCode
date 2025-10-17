class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        wordDict = set(wordDict)

        @cache
        def dp(idx, word):
            if idx == n:
                return word == ""

            ch = s[idx]
            partition = continu = False
            if (word + ch) in wordDict:
                partition = dp(idx + 1, "")
            continu = dp(idx + 1, word + ch)

            return partition or continu

        return dp(0, "")
