class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        maxNum, maxIdx = nums[0], 0
        minNum, minIdx = nums[0], 0

        for i, num in enumerate(nums):
            if maxNum < nums[i]:
                maxNum = num
                maxIdx = i
            if minNum > nums[i]:
                minNum = num
                minIdx = i

        ans = n

        if maxIdx < minIdx:
            ans = min(ans, maxIdx + (n - minIdx) + 1)
            ans = min(ans, minIdx + 1, n - maxIdx)
        elif maxIdx > minIdx:
            ans = min(ans, minIdx + (n - maxIdx) + 1)
            ans = min(ans, maxIdx + 1, n - minIdx)

        return ans
