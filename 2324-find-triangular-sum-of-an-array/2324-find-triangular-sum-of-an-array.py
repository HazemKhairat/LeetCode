class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            new_arr = []
            for i in range(len(nums) - 1):
                num = (nums[i] + nums[i + 1]) % 10
                new_arr.append(num)
            nums = new_arr
        
        return nums[0]
        