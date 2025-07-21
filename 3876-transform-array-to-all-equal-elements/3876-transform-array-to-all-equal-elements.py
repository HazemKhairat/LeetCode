class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:

        def solve(sign, nums):
            ops = 0
            for i in range(len(nums) -  1):
                if nums[i] != sign:
                    ops += 1
                    nums[i] *= -1
                    nums[i + 1] *= -1
            return ops if nums[-1] == sign else float(inf)
    
        return solve(-1, nums[:]) <= k or solve(1, nums[:]) <= k
            
        