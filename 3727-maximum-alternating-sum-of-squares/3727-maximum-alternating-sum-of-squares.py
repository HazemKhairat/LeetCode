class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums) // 2
        nums = [num * num for num in nums]
        nums.sort()
        postive = sum(nums[n:])
        negative = sum(nums[:n])
        return postive - negative
