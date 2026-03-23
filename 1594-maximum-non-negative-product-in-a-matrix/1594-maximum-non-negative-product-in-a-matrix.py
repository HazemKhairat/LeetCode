class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        
        @cache
        def solve(r, c, prod):
            if r == n or c == m:
                return -10000000
            if r == n - 1 and c == m - 1:
                tmp = prod * grid[r][c]
                if tmp >= 0:
                    return tmp 
                else:
                    return -1
            
            right = solve(r, c + 1, grid[r][c] * prod)
            down = solve(r + 1, c, grid[r][c] * prod)

            return max(right, down)
        ans = max(solve(0 ,0, 1), -1)
        return ans % (10**9 + 7) if ans >= 0 else ans

