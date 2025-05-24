class Solution:
    

    def numTrees(self, n: int) -> int:
        
        memo = {}

        def solve(n):

            if n == 0 or n == 1:
                return 1

            if n in memo:
                return memo[n]

            root = 0
            for i in range(1, n + 1):
                root += solve(i - 1) * solve(n - i)

            memo[n] = root
            return root

        return solve(n)