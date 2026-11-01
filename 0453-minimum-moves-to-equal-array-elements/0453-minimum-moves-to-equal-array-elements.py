class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini = min(nums)
        return sum([num - mini for num in nums])
