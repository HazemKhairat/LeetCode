class Solution:
    def minCost(self, n: int) -> int:

        ans = 0
        for i in range(n - 1, -1, -1):
            ans += i
        return ans