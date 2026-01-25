class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        f, s = 0, k - 1
        ans = inf
        while s < len(nums):
            ans = min(ans, nums[s] - nums[f])
            f += 1
            s += 1
        return ans
