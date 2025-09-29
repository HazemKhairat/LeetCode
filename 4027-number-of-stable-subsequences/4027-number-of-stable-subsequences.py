class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        odd = odd_odd = even = even_even = 0
        mod = 10**9 + 7

        for num in nums:
            if num % 2 == 0:
                even_even += even % mod
                even += (1 + odd + odd_odd) % mod
            else:
                odd_odd += odd % mod
                odd += (1 + even + even_even) % mod
        
        return (even + even_even + odd + odd_odd) % mod

