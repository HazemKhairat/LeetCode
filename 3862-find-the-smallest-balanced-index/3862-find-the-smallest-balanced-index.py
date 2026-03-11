class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefSum, suffProd = sum(nums), 1
        MAX = 2**63 - 1
        ans = -1

        for i in range(n - 1, -1, -1):
            prefSum -= nums[i]
            if prefSum == suffProd:
                ans = i
            if suffProd * nums[i] < MAX:
                suffProd *= nums[i]
            else:
                break

        return ans
