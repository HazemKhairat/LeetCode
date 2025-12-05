class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [nums[0]]
        for i in range(1, n):
            pref.append(nums[i] + pref[i - 1])

        suff = [0] * n
        suff[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i] + suff[i + 1]
        
        ans = 0
        for i in range(n - 1):
            if (pref[i] - suff[i + 1]) % 2 == 0:
                ans += 1
        
        return ans