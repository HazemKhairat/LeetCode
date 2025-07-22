class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        res = -inf
        maxi = mini = nums[0]

        for i in range(m - 1, len(nums)):
            maxi = max(maxi, nums[i - m + 1])
            mini = min(mini, nums[i - m + 1])
            res = max(res, nums[i] * maxi, nums[i] * mini)

        return res