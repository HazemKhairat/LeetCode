class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        add = inf
        for i in range(1, len(nums)):
            for j in range(i + 1, len(nums)):
                add = min(add, nums[j] + nums[i])

        return ans + add