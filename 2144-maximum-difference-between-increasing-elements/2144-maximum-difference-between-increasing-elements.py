class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans, prev = -1, nums[0]

        for j in range(1, n):
            if nums[j] > prev:
                ans = max(ans, nums[j] - prev)
            else:
                prev = nums[j]
            
        return ans

