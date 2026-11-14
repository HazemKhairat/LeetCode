class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = inf
        for i in range(n):
            size = l
            while True:
                if size > r or i + size > n:
                    break
               
                curr = sum(nums[i:i + size])
                if curr > 0:
                    ans = min(ans, curr)
                size += 1
        return ans if ans != inf else -1
                