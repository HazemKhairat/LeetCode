class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = Counter()
        maxElement = max(nums)
        res = 0
        i = 0

        for j in range(n):
            cnt[nums[j]] += 1
            while i <= j and cnt[maxElement] >= k:
                cnt[nums[i]] -= 1
                res += n - j
                i += 1

        return res
