class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 1
        maxi = max(nums)
        n = len(nums)
        i = 0
        while i < n - 1:
            l = 1
            ok = False
            while i < n - 1 and nums[i] == maxi and nums[i] == nums[i + 1]:
                l += 1
                i += 1
                ok = True
            res = max(res, l)
            if not ok:
                i += 1
        return res
