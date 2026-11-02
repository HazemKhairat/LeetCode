class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()

        def calc(i):
            nums_copy = nums[::]
            ans = 0
            for j in range(i, 0, -1):
                ans += nums_copy[j] - nums_copy[j - 1]
                nums_copy[j - 1] = nums_copy[j]
            for j in range(i + 1, n):

                ans += nums_copy[j] - nums_copy[j - 1]
                nums_copy[j] = nums_copy[j - 1]

            return ans

        if n % 2 == 0:
            f = calc((n // 2) - 1)
            s = calc(n // 2)
            return min(f, s)

        return calc(n // 2)

