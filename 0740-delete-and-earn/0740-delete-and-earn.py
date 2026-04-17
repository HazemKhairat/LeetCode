class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        freq = Counter(nums)
        arr = list(freq.keys())
        arr.sort()

        n = len(arr)

        dp = [0] * n
        dp[0] = arr[0] * freq[arr[0]]
        # print(arr)

        for i in range(1, n):
            val = arr[i] * freq[arr[i]]

            if arr[i] == arr[i - 1] + 1:
                skip = dp[i - 1]
                take = (dp[i - 2] if i > 1 else 0) + val
                dp[i] = max(take, skip)
            else:
                dp[i] = val + dp[i - 1]

        # print(dp)
        return dp[n - 1]
