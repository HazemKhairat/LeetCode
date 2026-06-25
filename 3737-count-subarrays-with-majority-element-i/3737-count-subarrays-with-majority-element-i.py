class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)

        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + (nums[i - 1] == target)
            

        ans = 0
        for i in range(n):
            for j in range(i, n):
                if pref[j + 1] - pref[i] > ((j - i + 1) // 2):
                    ans += 1
                
        return ans