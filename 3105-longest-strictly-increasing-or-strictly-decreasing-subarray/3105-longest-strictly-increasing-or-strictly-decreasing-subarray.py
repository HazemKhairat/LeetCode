class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        res = 1
        maxi = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                maxi += 1
                res = max(res, maxi)
            else:
                maxi = 1

        maxi = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                maxi += 1
                res = max(res, maxi)
            else:
                maxi = 1
        
        return res
                