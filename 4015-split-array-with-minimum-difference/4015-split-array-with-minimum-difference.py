class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left = [True] * n
        right = [True] * n

        for i in range(1, n):
            left[i] = left[i - 1] and nums[i] > nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] and nums[i] > nums[i + 1]

        # print(left)
        # print(right)

        total = sum(nums)
        pref_left = 0
        ans = inf

        for i in range(n - 1):
            pref_left += nums[i]
            if left[i] and right[i + 1]:
                right_pref = total - pref_left
                ans = min(ans, abs(right_pref - pref_left))

        return ans if ans != inf else -1
