class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        pref = [0] * (n)
        suff = [0] * (n)

        pref[0] = 1 if nums[0] == 1 else 0
        for i in range(1, n):
            if nums[i] == 0:
                pref[i] = 0
            else:
                pref[i] = 1 + pref[i - 1]

        maxi = max(pref) - 1
        suff[n - 1] = 1 if nums[-1] == 1 else 0
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                suff[i] = 0
            else:
                suff[i] = 1 + suff[i + 1]

        for i in range(n):
            if nums[i] == 0 and i == 0:
                maxi = max(maxi, suff[i + 1])
            elif nums[i] == 0 and i == n - 1:
                maxi = max(maxi, pref[i - 1])
            elif nums[i] == 0:
                maxi = max(maxi, pref[i - 1] + suff[i + 1])

        return maxi
