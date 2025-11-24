class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        ans = [False] * n
        tmp = 0
        for i, num in enumerate(nums):
            tmp = (tmp << 1) | num
            ans[i] = tmp % 5 == 0
        return ans
