class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[[None] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]


        def solve(idx1, idx2, k):
            if k == 0:
                return 0
            if idx1 == n or idx2 == m:
                return -(2**53 - 1)

            if dp[idx1][idx2][k] != None:
                return dp[idx1][idx2][k]

            take = (nums1[idx1] * nums2[idx2]) + solve(idx1 + 1, idx2 + 1, k - 1)
            skip1 = solve(idx1 + 1, idx2, k)
            skip2 = solve(idx1, idx2 + 1, k)

            dp[idx1][idx2][k] = max(take, skip1, skip2)
            return dp[idx1][idx2][k]

        return solve(0, 0, k)
