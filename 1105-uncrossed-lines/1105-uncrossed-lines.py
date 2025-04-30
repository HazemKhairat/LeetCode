class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        memo = [[-1] * (m + 1) for _ in range(n + 1)]

        def solve(i, j):
            if i == n or j == m:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            equal, tryI, tryJ = 0, 0, 0
            if nums1[i] == nums2[j]:
                equal = 1 + solve(i + 1, j + 1)
            tryI = solve(i + 1, j)
            tryJ = solve(i, j + 1)

            memo[i][j] = max(equal, tryI, tryJ)
            return memo[i][j]

        return solve(0, 0)
