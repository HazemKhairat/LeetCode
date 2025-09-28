class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        ans = 0
        for i in range(1, len(nums) - 1):
            if nums[i] + nums[i - 1] > nums[i + 1]:
                perimeter = nums[i] + nums[i - 1] + nums[i + 1]
                ans = max(ans, perimeter)

        return ans
