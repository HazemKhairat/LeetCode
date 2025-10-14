class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        for i in range(n - (2 * k) + 1):
            l = i
            r = (i + (2 * k)) - 1
            ok = True
            while l < (i + k - 1):
                if nums[l] >= nums[l + 1] or nums[r] <= nums[r - 1]:
                    ok = False
                l += 1
                r -= 1

            if ok:
                return True

        return False
