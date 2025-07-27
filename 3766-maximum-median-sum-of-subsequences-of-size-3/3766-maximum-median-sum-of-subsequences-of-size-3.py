class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i, j= 0, n - 1
        ans = 0

        while i < j:
            ans += nums[j - 1]
            i += 1
            j -= 2
            
        return ans