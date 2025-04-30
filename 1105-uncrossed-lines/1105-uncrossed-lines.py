class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                dp[i + 1][j + 1] = (
                    1 + dp[i][j] if x == y else max(dp[i][j + 1], dp[i + 1][j])
                )

        return dp[-1][-1]
