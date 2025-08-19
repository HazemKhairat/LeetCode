class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        ans = 0
        
        while r < len(nums):
            if nums[r] == 0:
                ans += r - l + 1
                r += 1
            else:
                r += 1
                l = r
            
        return ans