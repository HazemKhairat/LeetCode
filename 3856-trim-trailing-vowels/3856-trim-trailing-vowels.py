class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = "aeiou"
        s = list(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in vowels:
                return ''.join(s[:i+1])

        return ""