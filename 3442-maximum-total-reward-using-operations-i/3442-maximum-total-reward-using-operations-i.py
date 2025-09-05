class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()

        n = len(rewardValues)
        maxVal = rewardValues[-1]
        dp = [[-1] * (maxVal + 1) for _ in range(n + 1)]

        def solve(idx, curr):
            if idx == n:
                return curr

            c = min(curr, maxVal)
            if dp[idx][c] != -1:
                return dp[idx][c]

            skip = solve(idx + 1, curr)
            take = curr

            if rewardValues[idx] > curr:
                take = solve(idx + 1, curr + rewardValues[idx])

            dp[idx][c] = max(take, skip)
            return dp[idx][c]

        return solve(0, 0)
