class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dp = {}
        n = len(arr)
        res = 1
        for num in arr:
            if (num - diff) in dp:
                dp[num] = dp[num - diff] + 1
            else:
                dp[num] = 1

            res = max(res, dp[num])

        return res
