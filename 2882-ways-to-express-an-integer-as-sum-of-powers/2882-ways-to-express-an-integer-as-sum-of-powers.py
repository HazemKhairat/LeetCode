class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        powers = []
        l = 1
        while l**x <= n:
            powers.append(l**x)
            l += 1
        
        @cache
        def solve(curr, n):
            power = curr ** x
            if n == 0:
                return 1
            if n < 0 or power > n:
                return 0
            
            take = solve(curr + 1, n - power)
            skip = solve(curr + 1, n)
            return (take + skip) % MOD

        return solve(1, n)