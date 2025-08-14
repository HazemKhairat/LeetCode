class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = -inf

        for i, num in enumerate(nums):
            prev = nums[i] = min(num + k, max(prev + 1, num - k))
        
        return len(set(nums))