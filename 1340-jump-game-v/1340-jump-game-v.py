class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        new_arr = [[num, idx] for idx, num in enumerate(arr)]
        new_arr.sort()

        dp = [1] * n
        for num, i in new_arr:
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[i] <= arr[j]:
                    break

                dp[i] = max(dp[i], dp[j] + 1)

            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[i] <= arr[j]:
                    break

                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
