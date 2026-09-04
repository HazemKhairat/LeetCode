class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefMax = [-inf] * n
        prefMin = [inf] * n
        prefMax[0], prefMin[-1] = nums[0], nums[-1]

        for i in range(1, n):
            prefMax[i] = max(prefMax[i - 1], nums[i])
            prefMin[n - i - 1] = min(prefMin[n - i], nums[n - i - 1])

        for i in range(n):
            curr = prefMax[i] - prefMin[i]
            if curr <= k:
                return i

        return -1
