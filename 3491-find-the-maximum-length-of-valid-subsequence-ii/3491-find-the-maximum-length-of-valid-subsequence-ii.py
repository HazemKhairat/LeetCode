
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        dp = [[0] * k for _ in range(k)]
        maxi = 1
        for num in nums:
            curr = num % k
            for prev in range(k):
                dp[curr][prev] = dp[prev][curr] + 1
                maxi = max(maxi, dp[curr][prev])
            
        return maxi
