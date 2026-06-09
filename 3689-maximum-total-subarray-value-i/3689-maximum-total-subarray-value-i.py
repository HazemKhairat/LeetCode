class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mini, maxi = min(nums), max(nums)
        return (maxi - mini) * k