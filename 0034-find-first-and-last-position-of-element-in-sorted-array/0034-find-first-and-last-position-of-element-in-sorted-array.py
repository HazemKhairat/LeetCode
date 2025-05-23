class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x, y = -1, -1
        n = len(nums)
        # ====================

        # lower_bound
        i, j = 0, n - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        if i < n and nums[i] == target:
            x = i
        # print(x)

        # ====================

        # upper_bound
        i, j = 0, n - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        if i - 1 < n and i - 1 >= 0 and nums[i - 1] == target:
            y = i - 1
        # print(y)

        # ====================

        return [-1, -1] if x == -1 or y == -1 else [x, y]
