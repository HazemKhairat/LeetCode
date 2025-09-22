class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        maxi = max(cnt.values())
        ans = 0
        for key, val in cnt.items():
            if maxi == val:
                ans += val

        return ans