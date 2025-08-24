class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums = [0] + nums + [0]
        n = len(nums)
        dp = []
        maxi = 0
        tmp = 0
        for i in range(n):
            if nums[i] == 0:
                dp.append(tmp)
                tmp = 0
            else:
                tmp += 1
        
        for i in range(1, len(dp)):
            maxi = max(maxi, dp[i] + dp[i - 1])

        return maxi - 1 if maxi == n - 2 else maxi