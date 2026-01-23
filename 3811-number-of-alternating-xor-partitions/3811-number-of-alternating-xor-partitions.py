class Solution:
    def alternatingXOR(self, nums: List[int], t1: int, t2: int) -> int:

        arr = [t1, t2]
        memo = {}
        MOD = 10**9 + 7

        def solve(currXor, idx, turn):
            if idx == len(nums):
                return currXor == arr[turn]

            key = (currXor, idx, turn)
            if key in memo:
                return memo[key]

            total = 0

            if currXor == arr[turn]:
                total += solve(nums[idx], idx + 1, 1 - turn)

            total += solve((currXor ^ nums[idx]), idx + 1, turn)
            memo[key] = total % MOD
            return total % MOD

        return solve(nums[0], 1, 0) % MOD
