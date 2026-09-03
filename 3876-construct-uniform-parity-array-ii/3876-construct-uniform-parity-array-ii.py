class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        mini = min(nums)
        if mini % 2: return True
        return all(num % 2 == 0 for num in nums)
