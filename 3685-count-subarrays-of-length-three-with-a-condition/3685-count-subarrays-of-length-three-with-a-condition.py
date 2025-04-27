class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l, r, res = 0, 2, 0

        while r < len(nums):
            if nums[l] + nums[r] == (nums[l + 1] / 2):
                res += 1
            l += 1
            r += 1
        return res
