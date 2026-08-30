class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        idxOfMax = nums.index(max(nums))
        idxOfMin = nums.index(min(nums))

        l = min(idxOfMin, idxOfMax)
        r = max(idxOfMin, idxOfMax)

        return min(r + 1, n - l, l + 1 + n - r)
