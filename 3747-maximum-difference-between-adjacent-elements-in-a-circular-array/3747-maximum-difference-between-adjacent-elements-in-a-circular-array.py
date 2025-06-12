class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            mod = (i + 1) % n
            diff = abs(nums[i] - nums[mod])
            res = max(res, diff)

        return res
