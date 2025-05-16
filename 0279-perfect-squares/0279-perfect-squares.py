class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1,101):
            squares.append(i*i)
        
        memo = [[-1 for _ in range(n + 1)] for _ in range(len(squares))]

        def solve(index, n):
            if n == 0:
                return 0
            if index == len(squares) or n < 0:
                return float('inf')
                  
            if memo[index][n] != -1:
                return memo[index][n]
            take = skip = 0

            take = 1 + solve(index, n - squares[index])
            skip = solve(index + 1, n)

            memo[index][n] = min(take, skip)
            return memo[index][n]
        
        return solve(0, n)