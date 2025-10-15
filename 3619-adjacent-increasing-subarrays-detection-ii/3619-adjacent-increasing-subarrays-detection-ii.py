class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        nums.append(-inf)
        n = len(nums)
        prev = cnt = ans = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                ans = max(ans, max(min(prev, cnt), cnt // 2))
                prev = cnt
                cnt = 1
            
        return ans