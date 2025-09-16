from typing import List

class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        odd = 0         
        odd_odd = 0        
        even = 0      
        even_even = 0      

        for x in nums:
            if x % 2 == 1:                        
                odd_odd += odd % MOD
                odd += (even + even_even + 1) % MOD
            else:            
                even_even += even % MOD
                even += (odd + odd_odd + 1) % MOD

        total = (odd + odd_odd + even + even_even) % MOD
        return total
