class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            curr = max(nums[: i + 1]) - min(nums[i:n])
            if curr <= k:
                return i

        return -1
