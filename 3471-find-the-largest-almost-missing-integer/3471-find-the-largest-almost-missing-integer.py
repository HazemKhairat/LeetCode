class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        n = len(nums)
        cnt = Counter()
        for i in range(n - k + 1):
            st = set(nums[i : i + k])
            for val in st:
                cnt[val] += 1

        ans = -1
        for key, val in cnt.items():
            if val == 1:
                ans = max(ans, key)

        return ans
