class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        mid = n // 2
        if n % 2 == 0:
            s[:mid] = sorted(s[:mid])
            s[mid:] = sorted(s[mid:], reverse=True)
        else:
            s[: mid] = sorted(s[: mid])
            s[mid + 1 :] = sorted(s[mid + 1 :], reverse=True)
        return "".join(s)