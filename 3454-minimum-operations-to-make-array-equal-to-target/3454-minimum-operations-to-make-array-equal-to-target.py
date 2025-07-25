class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:

        prevPos = prevNeg = res = 0
        for i in range(len(nums)):
            diff = nums[i] - target[i]
            if diff < 0:
                if diff < prevNeg:
                    res += abs(diff - prevNeg)
                prevNeg = diff
                prevPos = 0
            elif diff > 0:
                if diff > prevPos:
                    res += abs(diff - prevPos)
                prevPos = diff
                prevNeg = 0
            else:
                prevPos = prevNeg = 0
        return res
