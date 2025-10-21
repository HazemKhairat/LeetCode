class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i, j = 0, len(s) - 1

        while i < j:
            while i < n and not s[i].isalpha():
                i += 1
            while j >= 0 and not s[j].isalpha():
                j -= 1

            if i < j:
                s[i], s[j] = s[j], s[i]

            i += 1
            j -= 1

        res = "".join(s)
        return res
