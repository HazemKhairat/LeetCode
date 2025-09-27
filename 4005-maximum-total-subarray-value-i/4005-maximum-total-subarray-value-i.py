class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mini = maxi = nums[0]
        mini = min(nums)
        maxi = max(nums)
        return (maxi - mini) * k