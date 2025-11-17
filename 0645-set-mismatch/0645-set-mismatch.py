class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = [0] + nums + [len(nums) + 1]
        nums.sort()
        ans = [0] * 2
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                ans[1] = nums[i] - 1
            elif nums[i] == nums[i - 1]:
                ans[0] = nums[i]
        return ans
