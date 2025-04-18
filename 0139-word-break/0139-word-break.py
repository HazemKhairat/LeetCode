class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def canBreak(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            # 0 1 2 3 4 5 6 7 8
            # l e e t c o d e
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and canBreak(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return canBreak(0)
