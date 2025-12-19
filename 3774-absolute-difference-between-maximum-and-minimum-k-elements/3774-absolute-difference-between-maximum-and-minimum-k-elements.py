class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        s = 0
        l = 0
        for i in range(k):
            s += nums[i]
        for i in range(n - 1, n - k - 1, -1):
            l += nums[i]
        return l - s