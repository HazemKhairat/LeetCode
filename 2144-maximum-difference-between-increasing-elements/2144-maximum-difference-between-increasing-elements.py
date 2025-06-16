class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        maxDiff = -1

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] <= nums[i]:
                    continue
                maxDiff = max(maxDiff, nums[j] - nums[i])

        return maxDiff
