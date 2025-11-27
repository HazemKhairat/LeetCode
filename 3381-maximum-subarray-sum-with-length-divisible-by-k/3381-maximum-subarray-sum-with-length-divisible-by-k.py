class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        nums = [0] + nums
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]

        res = [0] * n
        for i in range(k, n):
            curr = nums[i] - nums[i - k]
            res[i] = max(curr, curr + res[i - k])

        ans = max(res[k:])
        return ans
