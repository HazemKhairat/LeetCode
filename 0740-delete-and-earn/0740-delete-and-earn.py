class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        freq = Counter(nums)
        arr = list(freq.keys())
        arr.sort()
        memo = {}

        def solve(idx, prevPicked):
            if idx == len(arr):
                return 0
            key = (idx, prevPicked)

            if key in memo:
                return memo[key]

            take = skip = 0

            if not prevPicked or arr[idx] != (arr[idx - 1] + 1):
                val = arr[idx] * freq[arr[idx]]
                take = val + solve(idx + 1, True)

            skip = solve(idx + 1, False)

            memo[key] = max(take, skip)
            return max(take, skip)

        return solve(0, False)
