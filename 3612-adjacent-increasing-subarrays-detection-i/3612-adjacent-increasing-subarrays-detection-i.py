class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i = 0
        if k == 1: return True
        while i <= n - (k * 2):
            l = i + 1
            f = True
            while l < (i + k):
                
                f = f and (nums[l] > nums[l - 1])
                l += 1

            r = l + 1
            s = True
            while r < n and r <= (l + k - 1):
              
                s = s and (nums[r] > nums[r - 1])
                r += 1

            if f and s:
                return True
            i += 1

        return False
