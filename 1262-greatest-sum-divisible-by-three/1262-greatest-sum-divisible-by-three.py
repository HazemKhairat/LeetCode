class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def solve(idx, rem):
            if idx == n:
                return rem if rem % 3 == 0 else -inf
            take = nums[idx] + solve(idx + 1, (rem + nums[idx]) % 3)
            skip = solve(idx + 1, rem)
            return max(take, skip)

        return solve(0, 0)
