class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        for i in range(n):
            if i == nums[i]:
                continue
            ans &= nums[i]
        
        return 0 if ans == -1 else ans