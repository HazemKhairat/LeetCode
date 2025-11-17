class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = maxi = 0
        for num in nums:
            if num == 1:
                maxi += 1
            else:
                ans = max(ans, maxi)
                maxi = 0
        return max(ans, maxi)