class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            tmp = nums[i]
            sum = 0
            while tmp:
                sum += tmp % 10
                tmp //= 10
            if sum == i:
                return i

        return -1