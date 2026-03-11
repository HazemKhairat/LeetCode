class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:

        n = len(nums)
        prefSum = [0] * (n + 1)
        suffProd = [1] * (n + 1)
        MAX = 2**63 - 1
        for i in range(1, n + 1):
            prefSum[i] = prefSum[i - 1] + nums[i - 1]
        for i in range(n - 1, -1, -1):
            if suffProd[i + 1] * nums[i] > MAX:
                suffProd[i] = MAX
            else:
                suffProd[i] = suffProd[i + 1] * nums[i]
        # print(prefSum)
        # print(suffProd)
        for i in range(1, n + 1):
            if prefSum[i - 1] == suffProd[i]:
                return i - 1

        return -1
