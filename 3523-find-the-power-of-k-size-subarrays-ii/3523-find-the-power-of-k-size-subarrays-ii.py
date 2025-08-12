class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums
        pref = [1] * n
        
        for i in range(1, n):
            if nums[i] == (nums[i - 1] + 1):
                pref[i] += pref[i - 1]
            
        pref = [0] + pref
        
        l, r = 1, k
        ans = []

        while r <= n:
            if pref[r] - pref[l] == k - 1:
                ans.append(nums[r - 1])
            else:
                ans.append(-1)
            l += 1
            r += 1
        
        return ans
