class Solution:
    def maxSum(self, nums: List[int]) -> int:
        PosNums = set([num for num in nums if num > 0])
        return max(nums) if len(PosNums) == 0 else sum(PosNums)
        