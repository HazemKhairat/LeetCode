from sortedcontainers import SortedSet


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ans = 1
        count = 1
        st = SortedSet(nums)
        n = len(st)

        for i in range(1, n):
            if st[i] == (st[i - 1] + 1):
                count += 1
            else:
                ans = max(ans, count)
                count = 1

        return max(ans, count)
