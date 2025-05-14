class Solution:
    
    def numTrees(self, n: int) -> int:
       


        dp = [0] * (n + 1)

        def solve(n):
            if n <= 1:
                return 1
            
            if dp[n]:
                return dp[n]
            res = 0
            for i in range(1, n + 1):
                dp[n] += solve(i - 1) * solve(n - i)
            return dp[n]
        
        return solve(n)