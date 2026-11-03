class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        return sum(maxi - num for num in nums)