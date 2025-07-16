class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even, odd, alternative = 0, 0, 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        
        turn = nums[0] % 2

        for num in nums:
            if num % 2 == turn:
                turn = not turn
                alternative += 1
        
        return max(alternative, even, odd)