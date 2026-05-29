class Solution:
    def minElement(self, nums: List[int]) -> int:
        


        def digits_to_sum(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total
        
        ans = inf
        for num in nums:
            ans = min(ans, digits_to_sum(num))
        
        return ans