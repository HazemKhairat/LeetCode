class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dis = i = 0
        while i < len(nums) and nums[i] != 1:
            i += 1
        i += 1
        
        while i < len(nums):
            if nums[i] == 1 and dis < k:
                return False
            elif nums[i] == 0:
                dis += 1
            else:
                dis = 0
            i += 1
        return True
            