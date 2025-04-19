class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        def search(element, l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= element:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        for i in range(n):
            low = search(lower - nums[i], i + 1, n - 1)
            high = search(upper - nums[i] + 1, i + 1, n - 1)
            ans += high - low

        return ans
