class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        i, j = 0, 0
        res = []

        while i < n and j < n:
            if nums[j] == key:
                if abs(i - j) <= k:
                    res.append(i)
                    i += 1
                elif i <= j:
                    i += 1
                else:
                    j += 1
            else:
                j += 1

        return res
