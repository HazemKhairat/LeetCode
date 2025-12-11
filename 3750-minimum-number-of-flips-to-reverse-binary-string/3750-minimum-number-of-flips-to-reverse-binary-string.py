class Solution:
    def minimumFlips(self, n: int) -> int:

        s = []
        while n:
            s.append(n & 1)
            n //= 2

        rev = s[::-1]
        ans = 0
        for i in range(len(s)):
            ans += rev[i] ^ s[i]

        return ans