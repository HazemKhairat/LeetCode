class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        st = set(nums)
        maxItem = max(nums)
        for i in range(1, maxItem + 2):
            if i not in st:
                return i
        
        return 1