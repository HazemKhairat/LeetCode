class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 0 1 2 3 4
        # 1 3 5 4 7
        # 1 2 3 3 4
        # 1 1 1 1 2

        n = len(nums)
        length = [1] * n
        count = [1] * n

        maxLength = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
                maxLength = max(maxLength, length[i])

        res = 0
        for i in range(n):
            if length[i] == maxLength:
                res += count[i]

        return res
