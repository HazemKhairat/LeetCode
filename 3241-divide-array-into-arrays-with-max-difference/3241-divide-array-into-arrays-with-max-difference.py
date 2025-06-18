class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append([nums[i], nums[i + 1], nums[i + 2]])

        return res
