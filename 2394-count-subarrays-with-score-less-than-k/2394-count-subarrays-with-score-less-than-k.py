class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 0 1 2
        # 1 1 1
        res = total = 0
        i = 0
        for j in range(n):
            total += nums[j]  #  3
            while i <= j and total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1

            res += j - i + 1

        return res
