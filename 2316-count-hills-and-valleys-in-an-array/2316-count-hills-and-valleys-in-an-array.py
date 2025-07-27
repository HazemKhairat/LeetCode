class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev, curr = 0, 1
        res = 0
        while curr < len(nums) - 1:
            if nums[curr] == nums[curr + 1]:
                curr += 1
                continue
            if nums[curr] > nums[prev] and nums[curr] > nums[curr + 1]:
                res += 1
            elif nums[curr] < nums[prev] and nums[curr] < nums[curr + 1]:
                res += 1
            prev = curr
            curr += 1


        return res