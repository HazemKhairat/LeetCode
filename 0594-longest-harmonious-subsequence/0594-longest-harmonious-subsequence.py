class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        i, j = 0, 0
        while i < n and j < n:
            mini = nums[i]
            maxi = nums[j]
            if maxi - mini < 1:
                j += 1
            elif maxi - mini > 1:
                i += 1
            else:
                res = max(res, j - i + 1)
                j += 1

        return res
