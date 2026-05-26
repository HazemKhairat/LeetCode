class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowers = set([ch for ch in word if ch.islower()])
        uppers = set([ch for ch in word if ch.isupper()])

        ans = 0
        for ch in lowers:
            if ch.upper() in uppers:
                ans += 1

        return ans
            