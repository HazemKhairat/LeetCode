class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        i, j = 0, 2
        res = 0
        while j < len(nums):
            if (nums[i] + nums[j]) * 2 == nums[j - 1]:
                res += 1
            i += 1
            j += 1

        return res