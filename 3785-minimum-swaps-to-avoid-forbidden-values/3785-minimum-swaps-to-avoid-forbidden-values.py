class Solution:
    def minSwaps(self, nums: List[int], forb: List[int]) -> int:
        n = len(nums)
        ans = 0
        _nums = Counter(nums)
        _forb = Counter(forb)
        _cnt = Counter()

        for num in nums:
            if _nums[num] > n - _forb[num]:
                return -1

        cnt = 0
        maxi = 0
        for i in range(n):
            if nums[i] == forb[i]:
                _cnt[nums[i]] += 1
                maxi = max(_cnt[nums[i]], maxi)
                cnt += 1
            
        return max((cnt + 1) // 2, maxi)

