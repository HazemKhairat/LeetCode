class Solution:
    def maxFrequency(self, nums: List[int], k: int, ops: int) -> int:
        maxi = max(nums) + k + 1
        cnt = [0] * (maxi + 1)
        
        for num in nums:
            cnt[num] += 1
        for i in range(1, maxi + 1):
            cnt[i] += cnt[i - 1]

        res = 0
        for i in range(maxi):
            left = max(1, i - k)
            right = min(maxi, i + k)
            total = cnt[right] - (cnt[left - 1] if left else 0)
            freq = cnt[i] - (cnt[i - 1] if i else 0)
            res = max(res, freq + min(ops, total - freq))

        return res
