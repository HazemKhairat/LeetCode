class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        ans = []
        pref = 0
        for num in nums:
            pref = (pref << 1) | num
            ans.append(pref % 5 == 0)
        return ans
