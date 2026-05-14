class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        nums.sort()

        for i in range(1, n - 1):
            if nums[i] != nums[i - 1] + 1:
                return False

        return nums[-1] == nums[-2] and nums[-1] == n - 1
