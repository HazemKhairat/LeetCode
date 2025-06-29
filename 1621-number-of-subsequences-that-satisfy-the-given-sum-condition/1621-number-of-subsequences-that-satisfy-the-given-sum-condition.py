class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9 + 7
        n = len(nums)
        Pow = [0] * (100010)
        Pow[0] = 1
        for i in range(1, len(Pow)):
            Pow[i] = (Pow[i - 1] % MOD) * 2

        l, r = 0, n - 1
        res = 0
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                p = r - l
                res += Pow[p] % MOD
                l += 1

        return res % MOD
