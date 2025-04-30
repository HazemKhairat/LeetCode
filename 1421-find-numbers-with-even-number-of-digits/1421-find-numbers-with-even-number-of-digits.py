class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for num in nums:
            cnt = 0
            while num:
                cnt += 1
                num //= 10
            if cnt % 2 == 0:
                res += 1
        return res
