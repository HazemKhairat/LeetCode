class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0

        for num in range(1, n + 1):
            length = num.bit_length()
            ans = ((ans << length) | num) % MOD

        return ans
