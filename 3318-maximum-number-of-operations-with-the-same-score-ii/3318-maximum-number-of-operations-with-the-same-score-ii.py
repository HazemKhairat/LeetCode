class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def solve(f, s, val, total):
            if f >= s:
                return total

            front = back = inside = total
            if nums[f] + nums[f + 1] == val:
                front = solve(f + 2, s, nums[f] + nums[f + 1], total + 1)
            if nums[s] + nums[s - 1] == val:
                back = solve(f, s - 2, nums[s] + nums[s - 1], total + 1)
            if nums[f] + nums[s] == val:
                inside = solve(f + 1, s - 1, nums[f] + nums[s], total + 1)

            return max(front, back, inside)

        front = solve(2, n - 1, nums[0] + nums[1], 1)
        back = solve(0, n - 3, nums[n - 1] + nums[n - 2], 1)
        inside = solve(1, n - 2, nums[0] + nums[-1], 1)

        return max(front, back, inside)
