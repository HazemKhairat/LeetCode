class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        badIdx, leftIdx, rightIdx, res = -1, -1, -1, 0

        for i, num in enumerate(nums):
            if not (minK <= num <= maxK):
                badIdx = i
            else:
                if num == minK:
                    leftIdx = i
                if num == maxK:
                    rightIdx = i
            res += max(0, (min(leftIdx, rightIdx) - badIdx))

        return res
