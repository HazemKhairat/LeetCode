class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        bits = [0] * 32

        def update(num, change):
            for i in range(32):
                if (num >> i) & 1:
                    bits[i] += change

        def calc():
            res = 0
            for i in range(32):
                if bits[i]:
                    res |= (1 << i)
            return res
            
        ans = inf
        while r < len(nums):
            update(nums[r], 1)
            while l <= r and calc() >= k:
                ans = min(ans, r - l + 1)
                update(nums[l], -1)
                l += 1
            
            r += 1

        return ans if ans != inf else -1
            