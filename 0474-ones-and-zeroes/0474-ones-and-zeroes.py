class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = []
        for s in strs:
            zeros, ones = 0, 0
            for ch in s:
                if ch == "1":
                    ones += 1
                else:
                    zeros += 1
            arr.append((zeros, ones))

        memo = {}
        def solve(m, n, idx):
            if m < 0 or n < 0:
                return -inf
            if idx == len(arr):
                return 0
            if (m, n, idx) in memo:
                return memo[(m, n, idx)]

            take = skip = 0

            take = 1 + solve(m - arr[idx][0], n - arr[idx][1], idx + 1)
            skip = solve(m, n, idx + 1)
            memo[(m, n, idx)] = max(take, skip)
            return max(take, skip)

        return solve(m, n, 0)
