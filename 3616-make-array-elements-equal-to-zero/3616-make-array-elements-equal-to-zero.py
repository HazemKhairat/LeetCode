class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        pref = [0] * (n + 1)
        suff = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + nums[i - 1]
        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1] + nums[i]
        
        for i in range(n):
            if nums[i] == 0 and (suff[i] - pref[i + 1]) == 0:
                ans += 2
            elif nums[i] == 0 and abs(suff[i] - pref[i + 1]) == 1:
                ans += 1
        
        return ans